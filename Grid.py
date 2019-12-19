'''
Created on 2019. 12. 18.

@author: dswhd


'''

import numpy as np
import cv2
from cv2.cv2 import kmeans

# Create a black image



img = cv2.imread('./result/Sprite-0005_result.jpg',cv2.IMREAD_GRAYSCALE)

height, width = img.shape

print(width,height)

number = 16



yy = int(height/number)
lasty = 0
lastx = 0
map = []
map.append([])
for i in range(number):
    xx = 0
    lastx = 0
    for j in range(5):
      #  img = cv2.line(img,(xx,0),(xx,height),(255,0,0),1)

        xx += int(width/5)
        print(lasty,yy,lastx,xx)
        dot = img[lasty:yy,lastx:xx]
        lastx = xx
        im = './obj/img'+str(i)+','+str(j)+'.jpg'
        #cv2.imshow(im,dot)
        cv2.imwrite(im, dot)
        
   # img = cv2.line(img,(0,yy),(width,yy),(255,0,0),1)
    lasty = yy
    yy += int(height/number)
    
   


cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()