from djitellopy import tello
from time import sleep

drone = tello.Tello()
drone.connect()
print("The Battery Percent (%) is: ", drone.get_battery())

drone.takeoff()
sleep(2)
drone.send_rc_control(-10, -50, -50, -5) #LR,FB,UD,YW
sleep(2)

drone.send_rc_control(0, -20, 0, 0)
sleep(2)

drone.land()

