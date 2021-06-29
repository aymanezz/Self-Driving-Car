from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2
import logging
from Hand_Coded import LaneFollower
import numpy as np
import spidev

spi_bus = 0
spi_device = 0
spi = spidev.SpiDev()
spi.open(spi_bus, spi_device)
spi.max_speed_hz = 1000000

def show_image(title, frame):

     cv2.imshow(title, frame)
     cv2.waitKey()
lane_follower = LaneFollower()
# initialize the camera and grab a reference to the raw camera capture
camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate = 32
rawCapture = PiRGBArray(camera, size=(640, 480))
# allow the camera to warmup
time.sleep(0.1)
# capture frames from the camera
for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
    # grab the raw NumPy array representing the image, then initialize the timestamp
    # and occupied/unoccupied text
    image = frame.array
    combo_image = lane_follower.follow_lane(image)
    time.sleep(0.1)
    steering_sngle = lane_follower.curr_steering_angle
    OldMax = 140
    OldMin = 60
    NewMax = 0
    NewMin = 114
    OldValue = steering_sngle
    OldRange = (OldMax - OldMin)
    if (OldRange == 0):
        NewValue = NewMin
    else:
        NewRange = (NewMax - NewMin)  
        NewValue = (((OldValue - OldMin) * NewRange) / OldRange) + NewMin
    
    # show the frame
    # clear the stream in preparation for the next frame
    val = int(NewValue)
    send_byte = val
    spi.xfer2([send_byte])
    # show the frame
    print(val+130)
    cv2.imshow("combo", combo_image)
    # clear the stream in preparation for the next frame
    rawCapture.truncate(0)
    # if the `q` key was pressed, break from the loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()

