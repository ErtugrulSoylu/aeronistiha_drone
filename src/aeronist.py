import random
from struct import calcsize
from dronekit import connect, VehicleMode
from pymavlink import mavutil
import math
import time
from tokenize import String
import keras_preprocessing.image
import tensorflow as tf
from keras.models import model_from_json
import cv2
from keras_preprocessing import image
import numpy as np
import os
import sys

class drone:
    def __init__(self, vehicle):
        self.vehicle = vehicle
        
    def arm_only(self):
        print("Basic pre-arm checks")
        # Don't try to arm until autopilot is ready
        while not self.vehicle.is_armable:
            print(" Waiting for vehicle to initialise...")
            time.sleep(1)

        print("Arming motors")
        # Copter should arm in GUIDED mode
        self.vehicle.mode    = VehicleMode("GUIDED")
        self.vehicle.armed   = True

        # Confirm vehicle armed before attempting to take off
        while not self.vehicle.armed:
            print(" Waiting for arming...")
            time.sleep(1)

    def arm_and_takeoff(self, aTargetAltitude):
        print("Basic pre-arm checks")
        # Don't try to arm until autopilot is ready
        while not self.vehicle.is_armable:
            print(" Waiting for vehicle to initialise...")
            time.sleep(1)
            
        print("Arming motors")
        # Copter should arm in GUIDED mode
        self.vehicle.mode    = VehicleMode("GUIDED")
        self.vehicle.armed   = True

        # Confirm vehicle armed before attempting to take off
        while not self.vehicle.armed:
            print(" Waiting for arming...")
            time.sleep(1)

        print("Taking off!")
        self.vehicle.simple_takeoff(aTargetAltitude) # Take off to target altitude

        # Wait until the vehicle reaches a safe height before processing the goto (otherwise the command
        #  after Vehicle.simple_takeoff will execute immediately).
        while True:
            print(" Altitude: ", self.vehicle.location.global_relative_frame.alt)
            #Break and return from function just below target altitude.
            if self.vehicle.location.global_relative_frame.alt>=aTargetAltitude*0.95:
                print("Reached target altitude")
                break
            time.sleep(1)

    def go_to(self, posx, posy, posz, yaw_rate):
        msg = self.vehicle.message_factory.set_position_target_local_ned_encode(
            0,
            0, 0,
            mavutil.mavlink.MAV_FRAME_LOCAL_NED, 
            0b0000011111111000,
            posx, posy, posz, #pozisyonlar(metre)
            0, 0, 0,#hizlar(metre/s)
            0, 0, 0,#akselarasyon(fonksiyonsuz)
            0, math.radians(yaw_rate))#yaw,yaw_rate(rad,rad/s)
        self.vehicle.send_mavlink(msg)

    def calculate_distance(self, posx, posy, posz):
        dx = pow(2, posx - self.vehicle.location.global_relative_frame.lat)
        dy = pow(2, posy - self.vehicle.location.global_relative_frame.lon)
        dz = pow(2, posz - self.vehicle.location.global_relative_frame.alt)
        
        return math.sqrt(dx + dy + dz)

    def distance_inplace(self, posx, posy, posz):
        return [
            posx - self.vehicle.location.global_relative_frame.lat,
            posy - self.vehicle.location.global_relative_frame.lon,
            posz - self.vehicle.location.global_relative_frame.alt
        ]

    def in_position(self, posx, posy, posz, loc):
        ifx = posx > loc.north - 0.3 \
            and posx < loc.north + 0.3
        ify = posy > loc.east - 0.3 \
            and posy < loc.east + 0.3
        ifz = posz > loc.down - 0.3 \
            and posz < loc.down + 0.3
        return ifx and ify and ifz

    def accelerated_go(self, posx, posy, posz):
        print('Calculating the speed..')
        while not self.in_position(posx, posy, posz):
            dist = self.distance_inplace(posx, posy, posz)
            print(dist[0], dist[1], dist[2])
            speed = [2.0 if abs(elem) > 30 else elem / 15.0 for elem in dist]
            print(speed[0], speed[1], speed[2])
            self.send_ned_velocity(speed[0], speed[1], speed[2])

    def send_ned_velocity(self, velocity_x, velocity_y, velocity_z):
        """
        Move vehicle in direction based on specified velocity vectors.
        This uses the SET_POSITION_TARGET_GLOBAL_INT command with type mask enabling only 
        velocity components 
        (http://dev.ardupilot.com/wiki/copter-commands-in-guided-mode/#set_position_target_global_int).
        
        Note that from AC3.3 the message should be re-sent every second (after about 3 seconds
        with no message the velocity will drop back to zero). In AC3.2.1 and earlier the specified
        velocity persists until it is canceled. The code below should work on either version 
        (sending the message multiple times does not cause problems).
        
        See the above link for information on the type_mask (0=enable, 1=ignore). 
        At time of writing, acceleration and yaw bits are ignored.
        """
        msg = self.vehicle.message_factory.set_position_target_global_int_encode(
            0,       # time_boot_ms (not used)
            0, 0,    # target system, target component
            mavutil.mavlink.MAV_FRAME_GLOBAL_RELATIVE_ALT_INT, # frame
            0b0000111111000111, # type_mask (only speeds enabled)
            0, # lat_int - X Position in WGS84 frame in 1e7 * meters
            0, # lon_int - Y Position in WGS84 frame in 1e7 * meters
            0, # alt - Altitude in meters in AMSL altitude(not WGS84 if absolute or relative)
            # altitude above terrain if GLOBAL_TERRAIN_ALT_INT
            velocity_x, # X velocity in NED frame in m/s
            velocity_y, # Y velocity in NED frame in m/s
            velocity_z, # Z velocity in NED frame in m/s
            0, 0, 0, # afx, afy, afz acceleration (not supported yet, ignored in GCS_Mavlink)
            0, 0)    # yaw, yaw_rate (not supported yet, ignored in GCS_Mavlink)
        self.vehicle.send_mavlink(msg)

    def immadiateLanding(self):
        print("Changing Mode to LAND...")
        self.vehicle.mode = VehicleMode("LAND")
        while self.vehicle.mode != VehicleMode("LAND"):
            time.sleep(1)
        print("Success!")

        while self.vehicle.location.global_relative_frame.alt >= 0.1:
            print(' Altitude: ', self.vehicle.location.global_relative_frame.alt)
            time.sleep(1)
        
        print('Landed')


    def tespit(self, model, path):
        if os.path.isfile(path) is False:
            return False
        img = image.load_img(path, target_size=(224,224))
        x = image.img_to_array(img)
        x = np.expand_dims(x, axis=0) / 255

        classes = model.predict(x)
        
        print(np.argmax(classes[0])==0, max(classes[0]))
        return np.argmax(classes[0]) == 0

    def foto_cek(self, cam):
        ret, frame = cam.read()
        # if not ret:
        #     print("failed to grab frame")
        #     return 0

        path = "img/taken_photo{}.jpg".format(random.randint(1,1))
        # cv2.imwrite(path, frame)
        print("{} written!".format(path))
        
        cam.release()
        return path

    def get_fire_loc(self, path):
        return [self.vehicle.location.local_frame.north, self.vehicle.location.local_frame.east, self.vehicle.location.local_frame.down - 3]

    def goruntu_isleme(self, cam, model):
        path = self.foto_cek(cam)
        print(path)
        if path == 0:
            return False
        if self.tespit(model, path) == 1:
            loc = self.get_fire_loc(path)
            self.go_to(loc[0], loc[1], loc[2], 0)
            print("im here!")
            return True
        
        # if os.path.isfile(path):
        #     os.remove(path)

        return False


    def havadaTurlama(self):
        model = model_from_json(open("inc/model_new.json", "r").read())
        model.load_weights("inc/fire_detection_weights.h5")
        
        cam = cv2.VideoCapture(0)
        
        self.arm_and_takeoff(5)
        location = self.vehicle.location.local_frame
        shift = 3
        
        while True:
            self.go_to(location.north + shift, location.east + shift, location.down, 0)
            while (self.vehicle.location.local_frame.north < location.north + shift - 0.3 \
                or self.vehicle.location.local_frame.east < location.east + shift - 0.3):
                time.sleep(1)
            
            if self.goruntu_isleme(cam, model):
                break

            self.go_to(location.north + shift, location.east - shift, location.down, 0)
            while (self.vehicle.location.local_frame.north < location.north + shift - 0.3 \
                or self.vehicle.location.local_frame.east > location.east - shift + 0.3):
                time.sleep(1)

            if self.goruntu_isleme(cam, model):
                break
            
            self.go_to(location.north - shift, location.east - shift, location.down, 0)
            while (self.vehicle.location.local_frame.north > location.north - shift + 0.3 \
                or self.vehicle.location.local_frame.east > location.east - shift + 0.3):
                time.sleep(1)
            
            if self.goruntu_isleme(cam, model):
                break

            self.go_to(location.north - shift, location.east + shift, location.down, 0)
            while (self.vehicle.location.local_frame.north > location.north - shift + 0.3 \
                or self.vehicle.location.local_frame.east < location.east + shift - 0.3):
                time.sleep(1)
            
            if self.goruntu_isleme(cam, model):
                break

            shift *= 1.33
        cam.release()
        cv2.destroyAllWindows()