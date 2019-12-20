'''
Created on 2019. 12. 20.

@author: dswhd
'''
import numpy as np
import cv2

img = cv2.imread('./obj/img7,4.jpg',cv2.IMREAD_GRAYSCALE)
kernel =  np.ones((3,3),np.uint8)

grad = cv2.erode(img,kernel,iterations = 4)

cv2.imshow('grad',grad)
cv2.waitKey(0)
cv2.destroyAllWindows()
