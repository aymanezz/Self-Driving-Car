
import pandas as pd
import os
import numpy as np
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import random
import cv2

datadir = "F:\GP2021\steps\DeepPiCar-master\driver\code\dATA"


columns = ['center', 'left', 'right', 'steering', 'throttle', 'reverse', 'speed']
data = pd.read_csv(os.path.join(datadir, 'driving_log.csv'), names = columns)
pd.set_option('display.max_colwidth', None)
data.head()

def load_img_steering(datadir, df):
  image_path = []
  steering = []
  for i in range(len(data)):
    indexed_data = data.iloc[i]
    center, left, right = indexed_data[0], indexed_data[1], indexed_data[2]
    image_path.append(os.path.join(datadir, center.strip()))
    steering.append(float(indexed_data[3]))

  image_paths = np.asarray(image_path)
  steerings = np.asarray(steering)
  return image_paths, steerings

image_paths, steerings = load_img_steering(datadir + '/IMG', data)



video_type = cv2.VideoWriter_fourcc(*'XVID')
video_overlay = cv2.VideoWriter("%s_overlay.avi" % ('video_file'), video_type, 20.0, (320, 240))

for i in range(len(image_paths)):
    original_image = mpimg.imread(image_paths[i])
    video_overlay.write(original_image)
video_overlay.release()
