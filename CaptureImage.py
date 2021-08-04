from djitellopy import tello
import cv2

drone = tello.Tello()
drone.connect()
print("The Battery Percent (%) is: ", drone.get_battery())

drone.streamon()

while True:
    img = drone.get_frame_read().frame
    cv2.imshow("Image", img)
    cv2.waitKey(1)
