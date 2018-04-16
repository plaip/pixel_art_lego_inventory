import sys
from collections import Counter

class BrickInventory():
    def __init__(self, image):
        self.img = image
        self.w, self.h, self.channels = self.img.shape
        self.total_pixels = self.w * self.h
        self.color = 0

    def build(self):
        print ("Height:", self.h "Width:", self.w)
