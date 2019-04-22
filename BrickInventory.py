import sys
from collections import Counter

class BrickInventory():
    def __init__(self, image):
        self.img = image
        self.w, self.h, self.channels = self.img.shape
        self.total_pixels = self.w * self.h
        self.color = 0
        self.brick_inventory = dict()

    def build(self):
        brick_length_temp = 1
        for y in range(0, self.h):
            for x in range(0, self.w):
                R = self.img[x-1,y-1,2]
                G = self.img[x-1,y-1,1]
                B = self.img[x-1,y-1,0]
                RGB_last_int = R << 16 + G << + B
                R = self.img[x,y,2]
                G = self.img[x,y,1]
                B = self.img[x,y,0]
                RGB_int = R << 16 + G << 8 + B
                # print ("RGB: ", RGB_int)
                # Check if the current pixel is different the previous pixel
                # It's used to compute the length of brick
                if RGB_int == RGB_last_int:
                    brick_length_temp += 1
                else :
                    if RGB_int in self.brick_inventory.values():
                        self.brick_inventory[str({R,G,B}), brick_length_temp] += 1
                    else:
                        self.brick_inventory[(str({R,G,B}), brick_length_temp)] = 1
                        # print ("{RGB: ", RGB_int, "Brick length: ", brick_length_temp, "Count: ", self.brick_inventory[(RGB_int, brick_length_temp)])
                        brick_length_temp = 1
            brick_length_temp = 1
        print("-------------------------------------------------------------")
        print(sorted(self.brick_inventory))
        print(sum(self.brick_inventory.values()))
        print(self.total_pixels)