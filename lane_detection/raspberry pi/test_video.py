import logging
from Hand_Coded import LaneFollower
import cv2
import numpy as np
import spidev
import time
spi_bus = 0
spi_device = 0

spi = spidev.SpiDev()

spi.open(spi_bus, spi_device)
spi.max_speed_hz = 1000000

def show_image(title, frame):

     cv2.imshow(title, frame)
     cv2.waitKey()

lane_follower = LaneFollower()
cap = cv2.VideoCapture("video6.mp4")
while(cap.isOpened()):

# starting time
    start = time.time()
    time.sleep(0.1)
    _, frame = cap.read()
    combo_image = lane_follower.follow_lane(frame)
    steering_sngle = lane_follower.curr_steering_angle
    OldMax = 130
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
    print(NewValue)

    #print(steering_sngle)
    val = int(NewValue)
    #value = val + st
    end = time.time()

# total time taken
    print(f" of the program is {end - start}")
    send_byte = val
    spi.xfer2([send_byte])
    print(val+130)
    cv2.imshow("Road with Lane line", combo_image)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()

