from dronekit import connect, VehicleMode, LocationGlobalRelative
from pymavlink import mavutil
import time

connection = None
simulation = True

if connection:
    vehicle = connection
elif simulation:
    vehicle = connect("127.0.0.1:14550")
    print('IHA SIMULASYON ORTAMINA HAZIR')
else:
    vehicle = connect("/dev/serial0", baudrate=57600)
    print('IHA PIXHAWKA BAGLANDI\n')

# vehicle.armed = True
# vehicle.mode = VehicleMode('GUIDED')
# vehicle.simple_takeoff(5)
def send_ned_velocity(velocity_x, velocity_y, velocity_z, duration):
    """
    Move vehicle in direction based on specified velocity vectors.
    """
    msg = vehicle.message_factory.set_position_target_local_ned_encode(
        0,       # time_boot_ms (not used)
        0, 0,    # target system, target component
        mavutil.mavlink.MAV_FRAME_LOCAL_NED, # frame
        0b0000111111000111, # type_mask (only speeds enabled)
        0, 0, 0, # x, y, z positions (not used)
        velocity_x, velocity_y, velocity_z, # x, y, z velocity in m/s
        0, 0, 0, # x, y, z acceleration (not supported yet, ignored in GCS_Mavlink)
        0, 0)    # yaw, yaw_rate (not supported yet, ignored in GCS_Mavlink)


    # send command to vehicle on 1 Hz cycle
    for x in range(0,duration):
        vehicle.send_mavlink(msg)
        time.sleep(1)

send_ned_velocity(10,10,0, 100)