'''
Created on 2019. 12. 21.

@author: dswhd
'''

import numpy as np
import datetime
from cv2 import *
now = datetime.datetime.now().strftime("%d_%H-%M-%S")
img_path = './img/'+str(now)+'.png'
filename, ext = os.path.splitext(os.path.basename(img_path))
src = []




def mouse_handler(event, x, y, flags, param):
 
  if event == cv2.EVENT_LBUTTONUP:
    img = ori_img.copy()

    src.append([x, y])
    
    for xx, yy in src:
      cv2.circle(img, center=(xx, yy), radius=5, color=(0, 255, 0), thickness=-1, lineType=cv2.LINE_AA)

    cv2.imshow('img', img)

    # perspective transform
    if len(src) == 4:
      src_np = np.array(src, dtype=np.float32)

      width = max(np.linalg.norm(src_np[0] - src_np[1]), np.linalg.norm(src_np[2] - src_np[3]))
      height = max(np.linalg.norm(src_np[0] - src_np[3]), np.linalg.norm(src_np[1] - src_np[2]))

      dst_np = np.array([
        [0, 0],
        [width, 0],
        [width, height],
        [0, height]
      ], dtype=np.float32)
      
      M1 = cv2.getPerspectiveTransform(src=src_np, dst=dst_np)
      result = cv2.warpPerspective(ori_img, M=M1, dsize=(width, height))
      
      cv2.imshow('result', result)
      cv2.imwrite('./result/%s_result%s' % (filename, ext), result)
      
      
cap = cv2.VideoCapture(0)

while cap.isOpened():
     success, frame = cap.read()
     if success:

        cv2.imshow('discode', frame)
       
        key = cv2.waitKey(1) & 0xFF
        if (key == 27): 
            break
        elif(key==32):
            print('capture')
            ori_img = imread(img_path)
            cv2.imwrite(img_path,frame)

cap.release()
cv2.destroyAllWindows()