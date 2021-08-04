from djitellopy import tello
import TelloKeyboardModel as km
from time import sleep

km.init()
drone = tello.Tello()
drone.connect()
print("The Battery Percent (%) is: ", drone.get_battery())

def getKeyboardInput():
    lr, fb, ud, yv = 0, 0, 0, 0
    speed = 30
    if km.getKey("LEFT"): lr = -speed
    elif km.getKey("RIGHT"): lr = speed
    if km.getKey("UP"): fb = speed
    elif km.getKey("DOWN"): fb = -speed
    if km.getKey("w"): ud = speed
    elif km.getKey("s"): ud = -speed
    if km.getKey("d"): yv = speed
    elif km.getKey("a"): yv = -speed
    if km.getKey("q"): drone.land()
    elif km.getKey("e"): drone.takeoff()

    return [lr, fb, ud, yv]

while True:
    vals = getKeyboardInput()
    drone.send_rc_control(vals[0], vals[1], vals[2], vals[3])
    sleep(0.05)