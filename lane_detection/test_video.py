import logging
from Hand_Coded import LaneFollower
import cv2
import numpy as np
def show_image(title, frame):

     cv2.imshow(title, frame)
     cv2.waitKey()

lane_follower = LaneFollower()
cap = cv2.VideoCapture("test2.mp4")
while(cap.isOpened()):
    _, frame = cap.read()
    combo_image = lane_follower.follow_lane(frame)
    cv2.imshow("Road with Lane line", combo_image)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
