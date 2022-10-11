# import tensorflow as tf
import numpy as np
import random
import math
import time
# import keras_preprocessing.image
# import cv2
import os
import sys
from pymavlink import mavutil
# from keras.models import model_from_json
# from keras_preprocessing import image

class drone:
    def __init__(self, connection=None, simulation=False, detailed=False):
        self.detailed = detailed
        
        if connection:
            self.connection = connection
        elif simulation:
            self.connection = mavutil.mavlink_connection("127.0.0.1:14550")
            self.connection.wait_heartbeat()
            print('IHA SIMULASYON ORTAMINA HAZIR')
        else:
            self.connection = mavutil.mavlink_connection("/dev/ttyAMA0")
            self.connection.wait_heartbeat()
            print('IHA PIXHAWKA BAGLANDI\n')

    def __detail(self, message):
        if self.detailed: print(message)

    def __resultMessage(self, command, success=True, failReason="BILINMEYEN BIR HATA"):
        if success:
            print(command, "KOMUTU ICRA EDILDI\n")
        else:
            print(command, "KOMUTU", failReason, "NEDENIYLE ICRA EDILEMEDI\n")

    def arm_only(self):
        """
            IHA'yi arm eder.
        """

        print("\nARM KOMUTU ALINDI")

        self.__detail("\ARM SINYALI GONDERILIYOR")
        self.connection.mav.command_long_send(self.connection.target_system,
            self.connection.target_component,
            mavutil.mavlink.MAV_CMD_COMPONENT_ARM_DISARM, 0, 1, 0, 0, 0, 0, 0, 0)
        self.__detail("\tARM SINYALI GONDERILDI\n")

        print("\tARAÇ ARM EDILIYOR")
        self.connection.motors_armed_wait()
        print("\tARAÇ ARM EDILDI")

        self.__resultMessage("ARM")

    def arm_and_takeoff(self, targetAltitude):
        """
            targetAltitude: IHA'nin metre cinsinden yukselmesi istenilen yukseklik.

            IHA arm edilir ve istenilen yukseklige ulasmak uzere kalkisa gecer. Yeterince
            yukselene kadar program bloklanir. 
        """
        
        print("\nTAKEOFF KOMUTU ALINDI: HEDEF_YÜKSEKLİK=%d Metre" %(targetAltitude))
        
        self.arm_only()

        self.__detail("\tTAKEOFF SINYALI GONDERILIYOR")
        self.connection.mav.command_long_send(self.connection.target_system,
            self.connection.target_component,
            mavutil.mavlink.MAV_CMD_NAV_TAKEOFF, 0, 0, 0, 0, 0, 0, 0, targetAltitude)
        self.__detail("\tTAKEOFF SINYALI GONDERILDI")

        print("\tARAÇ YÜKSELİYOR")
        while 1:
            msg = self.connection.recv_match(
                type='LOCAL_POSITION_NED', blocking=True)
            print('\t\tYUKSEKLIK: %f metre' %(-msg.z))
            if -msg.z > targetAltitude * 0.98:
                break
        print('\tHEDEF YÜKSEKLİĞE ULAŞILDI')

        self.__resultMessage("TAKEOFF")

    def changeVehicleMode(self, mode : str):
        """
            mode: Gecis yapilacak mod

            IHA'nin istenilen moda gecirilmesini saglar. Moda gecilene kadar program bloklanir.
            Eger istenilen mod gecerli degilse hata mesaji dondurur.
        """

        print("\nMOD DEGISTIRME KOMUTU ALINDI: HEDEF MOD=\"%s\"" %(mode))

        if mode not in self.connection.mode_mapping():
            print("BILINMEYEN MOD : {}".format(mode))
            print("UYGUN MODLAR : ", list(self.connection.mode_mapping().keys()))
            self.__resultMessage("MOD DEGISTIRME", success=False, failReason="BILINMEYEN MOD")
            return

        mode_id = self.connection.mode_mapping()[mode]
        self.__detail("\tMOD DEGISTIRME SINYALI GONDERILIYOR")
        self.connection.set_mode(mode_id)
        self.__detail("\tMOD DEGISTIRME SINYALI GONDERILDI")

        print("\tMOD DEGISIMI BEKLENIYOR")
        while True:
            ack_msg = self.connection.recv_match(type="COMMAND_ACK", blocking=True)
            ack_msg = ack_msg.to_dict()

            if ack_msg["command"] != mavutil.mavlink.MAV_CMD_DO_SET_MODE:
                continue

            self.__detail(mavutil.mavlink.enums["MAV_RESULT"][ack_msg["result"]].description)
            print("\tMOD DEGISTIRILDI YENI MOD:\"%s\"" %(mode))

            break

        self.__resultMessage("MOD DEGISTIRME")

    def immadiateLanding(self):
        """
            Ani inis modu. IHA inise zorlanir, inis yapilana kadar program bloklanir.        
        """

        print("\nACIL INIS KOMUTU ALINDI")

        self.changeVehicleMode("LAND")

        print("\tIHA INISE GECIYOR")
        while 1:
            msg = self.connection.recv_match(
                type='LOCAL_POSITION_NED', blocking=True)
            print('\t\tYUKSEKLIK: %f metre' %(-msg.z))
            if -msg.z > 0.1:
                break
        print('\tIHA BASARIYLA INIS YAPTI')
        
        self.__resultMessage("ACIL INIS")

    def move(self, x, y, z, vx=0, vy=0, vz=0, afx=0, afy=0, afz=0, yaw=0, yaw_rate=0, coordinate_frame=mavutil.mavlink.MAV_FRAME_LOCAL_NED, type_mask=int(0b110111111000)):
        """
            x, y, z: Gidilecek koordinatlar
            vx, vy, vz: Hizlar
            afx, afy, afz: Ivmeler
            yaw: Donus hizi
            yaw_rate: Donus frekansi
            coordinate_frame: Koordinatlarin tipi (global veya yerel koordinatlar gibi)

            Istenilen koordinatlara gidilmesini saglar. Noktaya ulasana kadar program bloklanir.
        """

        print('\nMOVE KOMUTU ALINDI')
        
        self.__detail('MOVE SINYALI GONDERILIYOR')
        self.connection.mav.send(mavutil.mavlink.MAVLink_set_position_target_local_ned_message(10, self.connection.target_system, self.connection.target_component,
            coordinate_frame, type_mask,
            x, y, z, #konum
            vx, vy, vz, #hiz
            afx, afy, afz, #ivme
            yaw, yaw_rate)) #yaw
        self.__detail('MOVE SINYALI GONDERILDI')

        print('\tIHA YOLA CIKIYOR')
        while 1:
            msg = self.connection.recv_match(
                type='LOCAL_POSITION_NED', blocking=True)

            distance = math.sqrt((msg.x - x) ** 2 + (msg.y - y) ** 2 + (msg.z - z) ** 2)
            print('\t\tKONUM: { x : %f, y : %f, z : %f } : HEDEFE UZAKLIK : %f' %(msg.x, msg.y, msg.z, distance))
            if distance < 0.1:
                print('\tHEDEFE ULASILDI')
                break

        self.__resultMessage('MOVE')

    def rotate(self, angle, angular_speed=25, direction=1, relative=1):
        """
            angle: Donulmesi istenilen aci degeri
            angular_speed: Acisal hiz
            direction: 1: Saat yonu, -1: Saat yonunun tersi
            relative: 0: Mutlak aci, 1: Bagimli aci
        """
        
        if direction:   print('\nROTATE KOMUTU ALINDI: %d DERECE SAAT YONUNDE DONULUYOR' %(angle))
        else:           print('\nROTATE KOMUTU ALINDI: %d DERECE SAAT YONUNUN TERSINE DONULUYOR' %(angle))
        
        self.__detail('ROTATE SINYALI GONDERILIYOR')
        self.connection.mav.command_long_send(self.connection.target_system,
            self.connection.target_component,
            mavutil.mavlink.MAV_CMD_CONDITION_YAW, 0,
            angle, angular_speed, direction, relative,
            0, 0, 0)
        self.__detail('ROTATE SINYALI GONDERILDI')

        print('\tIHA DONUSE BASLIYOR')
        
        for i in range(3, 0, -1):
            print('\t\tGERI SAYIM, %d' %(i))
            time.sleep(1)

        while 1:
            msg = self.connection.recv_match(
                type='ATTITUDE', blocking=True)

            print('\t\tDONUS HIZI: %f' %(msg.yawspeed))
            if abs(msg.yawspeed) < 0.01:
                print('\tDONUS TAMAMLANDI')
                break

        self.__resultMessage('ROTATE')

    # def tespit(self, model, path):
    #     if os.path.isfile(path) is False:
    #         return False
    #     img = image.load_img(path, target_size=(224,224))
    #     x = image.img_to_array(img)
    #     x = np.expand_dims(x, axis=0) / 255

    #     classes = model.predict(x)
        
    #     print(np.argmax(classes[0])==0, max(classes[0]))
    #     return np.argmax(classes[0]) == 0

    # def foto_cek(self, cam):
    #     ret, frame = cam.read()
    #     # if not ret:
    #     #     print("failed to grab frame")
    #     #     return 0

    #     path = "img/taken_photo{}.jpg".format(random.randint(1,1))
    #     # cv2.imwrite(path, frame)
    #     print("{} written!".format(path))
        
    #     cam.release()
    #     return path

    # def get_fire_loc(self, path):
    #     return [self.vehicle.location.local_frame.north, self.vehicle.location.local_frame.east, self.vehicle.location.local_frame.down - 3]

    # def goruntu_isleme(self, cam, model):
    #     path = self.foto_cek(cam)
    #     print(path)
    #     if path == 0:
    #         return False
    #     if self.tespit(model, path) == 1:
    #         loc = self.get_fire_loc(path)
    #         self.go_to(loc[0], loc[1], loc[2], 0)
    #         print("im here!")
    #         return True
        
    #     # if os.path.isfile(path):
    #     #     os.remove(path)

    #     return False


    # def havadaTurlama(self):
    #     model = model_from_json(open("inc/model_new.json", "r").read())
    #     model.load_weights("inc/fire_detection_weights.h5")
        
    #     cam = cv2.VideoCapture(0)
        
    #     self.arm_and_takeoff(5)
    #     location = self.vehicle.location.local_frame
    #     shift = 3
        
    #     while True:
    #         self.go_to(location.north + shift, location.east + shift, location.down, 0)
    #         while (self.vehicle.location.local_frame.north < location.north + shift - 0.3 \
    #             or self.vehicle.location.local_frame.east < location.east + shift - 0.3):
    #             time.sleep(1)
            
    #         if self.goruntu_isleme(cam, model):
    #             break

    #         self.go_to(location.north + shift, location.east - shift, location.down, 0)
    #         while (self.vehicle.location.local_frame.north < location.north + shift - 0.3 \
    #             or self.vehicle.location.local_frame.east > location.east - shift + 0.3):
    #             time.sleep(1)

    #         if self.goruntu_isleme(cam, model):
    #             break
            
    #         self.go_to(location.north - shift, location.east - shift, location.down, 0)
    #         while (self.vehicle.location.local_frame.north > location.north - shift + 0.3 \
    #             or self.vehicle.location.local_frame.east > location.east - shift + 0.3):
    #             time.sleep(1)
            
    #         if self.goruntu_isleme(cam, model):
    #             break

    #         self.go_to(location.north - shift, location.east + shift, location.down, 0)
    #         while (self.vehicle.location.local_frame.north > location.north - shift + 0.3 \
    #             or self.vehicle.location.local_frame.east < location.east + shift - 0.3):
    #             time.sleep(1)
            
    #         if self.goruntu_isleme(cam, model):
    #             break

    #         shift *= 1.33
    #     cam.release()
    #     cv2.destroyAllWindows()