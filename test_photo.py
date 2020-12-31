import logging
from Hand_Coded import LaneFollower
import cv2
import numpy as np
def show_image(title, frame):

     cv2.imshow(title, frame)
     cv2.waitKey()

def test_photo(file):

    lane_follower = LaneFollower()
    frame = cv2.imread(file)
    combo_image = lane_follower.follow_lane(frame)
    cv2.imshow('final', combo_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

test_photo('test2_000_085.png')
