import sys
import cv2
from pathlib import Path
import numpy as np
from BackgroundColorDetector import BackgroundColorDetector

#TODO replace by argPArse
picture_path = Path(sys.argv[1])

if picture_path.is_file():
  print (picture_path)
  picture_path = str(picture_path)  # <--- convert to string
  image = cv2.imread(picture_path)
  print (image.size)                # Get the width and hight of the image for iterating over

  BackgroundColor = BackgroundColorDetector(picture_path)
  if BackgroundColor.detect() == 0:

