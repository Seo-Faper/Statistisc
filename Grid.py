'''
Created on 2019. 12. 18.

@author: dswhd


'''

import numpy as np
import cv2
from cv2.cv2 import kmeans

# Create a black image


def SetGrid(imgPath,size):
    img = cv2.imread(imgPath)

    height, width,shape = img.shape

    print(width,height)

    number = size



    yy = int(height/number)
    lasty = 0
    lastx = 0
    map = []
    img = cv2.line(img,(0,0),(width,0),(0,0,0),2)
    img = cv2.line(img,(0,0),(0,height),(0,0,0),2)
    map.append([])
    for i in range(number):
        img = cv2.line(img,(0,yy),(width,yy),(0,0,0),2)
        xx = 0
        lastx = 0
        for j in range(5):
            img = cv2.line(img,(xx,0),(xx,height),(0,0,0),2)

            xx += int(width/5)
            print(lasty,yy,lastx,xx)
            dot = img[lasty:yy,lastx:xx]

            lastx = xx
            im = './obj/img'+str(i)+','+str(j)+'.jpg'
            # cv2.imshow(im,dot)
            img = cv2.line(img,(xx,0),(xx,height),(0,0,0),2)
            kernel =  np.ones((3,3),np.uint8)
            dot = cv2.erode(dot,kernel,iterations = 4)
            cv2.imwrite(im, dot)
        
        img = cv2.line(img,(0,yy),(width,yy),(0,0,0),2)
        lasty = yy
        yy += int(height/number)
    
   


    cv2.imshow('image', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
SetGrid('./result/3_result.jpg', 16)