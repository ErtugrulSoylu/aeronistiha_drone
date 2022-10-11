from aeronist import drone

vehicle = drone(simulation=True)
vehicle.changeVehicleMode('GUIDED')
vehicle.arm_and_takeoff(5)
vehicle.move(5, 10, -4)