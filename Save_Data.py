import logging
from Hand_Coded import LaneFollower
import cv2
import numpy as np
import os
def show_image(title, frame):

     cv2.imshow(title, frame)
     cv2.waitKey()

def save_Data(video_file):
    lane_follower = LaneFollower()
    cap = cv2.VideoCapture(video_file)

    try:
        i = 0
        while cap.isOpened():
            _, frame = cap.read()
            combo_image = lane_follower.follow_lane(frame)
            cv2.imshow("result", combo_image)
            directory = "F:\GP2021\SDC\lane_follower\data"
            # Change the current directory
            # to specified directory
            os.chdir(directory)
            print("Before saving image:")
            print(os.listdir(directory))

            cv2.imwrite("%s_%03d_%03d.png" % (video_file, i,
                                              lane_follower.curr_steering_angle),
                                               frame)
            i += 1


            if cv2.waitKey(1) & 0xFF == ord('q'):

                break
    finally:
        cap.release()
        cv2.destroyAllWindows()

save_Data("test2.mp4")
