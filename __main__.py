import sys
import cv2
from pathlib import Path
import numpy as np
from BackgroundColorDetector import BackgroundColorDetector
from BrickInventory import BrickInventory
from PIL import Image

#TODO replace by argPArse
picture_path = Path(sys.argv[1])

if picture_path.is_file():
  print (picture_path)
  picture_path = str(picture_path)  # <--- convert to string
  image_cv = cv2.imread(picture_path)
  image_cv = cv2.cvtColor(image_cv, cv2.COLOR_BGR2RGB)
  image = Image.open(picture_path)
  pixel = image.load()

  RGBValues = ("27,42,52","100,100,100","150,150,150","200,200,200","244,244,244","114,0,18","180,0,0","55,33,0","95,49,9","119,119,78","137,125,98","176,160,111","145,80,28","187,128,90","170,125,85","252,172,0","41,100,99","255,201,149","250,200,10","255,236,108","245,243,215","0,69,26","112,142,124","0,133,43","88,171,65","165,202,24","226,249,154","70,155,195","104,195,226","25,50,90","30,90,168","115,150,200","112,129,154","157,195,247","211,242,234","68,26,145","144,31,118","160,110,185","205,164,222","211,53,157","255,158,205")
  ColorNames = ("Black","Dark Stone Grey","Medium Stone Grey","Light Stone Grey","White","New Dark Red","Bright Red","Dark Brown","Reddish Brown","Olive Green","Sand Yellow","Brick Yellow","Dark Orange","Nougat","Medium Nougat","Bright Orange","Flame Yellowish Orange","Light Nougat","Bright Yellow","Cool Yellow","White Glow","Earth Green","Sand Green","Dark Green","Bright Green","Bright Yellowish Green","Spring Yellowish Green","Dark Azur","Medium Azur","Earth Blue","Bright Blue","Medium Blue","Sand Blue","Light Royal Blue","Aqua","Medium Lilac","Bright Reddish Violet","Medium Lavender","Lavender","Bright Purple","Light Purple")
  ColorCodes = [26,199,194,208,1,154,21,308,192,330,138,5,38,18,312,106,191,283,24,226,329,141,151,28,37,119,326,321,322,140,23,102,135,212,323,268,124,324,325,221,222]

  ColorPalette= Image.new("P", (1,1))
  ColorPalette.putpalette( (27,42,52, 100,100,100, 150,150,150, 200,200,200, 244,244,244, 114,0,18, 180,0,0, 55,33,0, 95,49,9, 119,119,78, 137,125,98, 176,160,111, 145,80,28, 187,128,90, 170,125,85, 214,121,35, 252,172,0, 255,201,149, 250,200,10, 255,236,108, 245,243,215, 0,69,26, 112,142,124, 0,133,43, 88,171,65, 165,202,24, 226,249,154, 70,155,195, 104,195,226, 25,50,90, 30,90,168, 115,150,200, 112,129,154, 157,195,247, 211,242,234, 68,26,145, 144,31,118, 160,110,185, 205,164,222, 211,53,157, 255,158,205) + (0,0,0)*215)

  #REDUCE COLORS
  converted = image.convert("RGB").quantize(palette=ColorPalette)
  pixel = converted.load()
  converted.show() #show converted image
  #image.show() #show origonal image

  print (image_cv.size)                # Get the width and hight of the image for iterating over

  BackgroundColor = BackgroundColorDetector(picture_path)
  if BackgroundColor.detect() == 0:
    BrickInventory = BrickInventory(converted)
    BrickInventory.build()