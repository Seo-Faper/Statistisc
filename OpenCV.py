import cv2, os
import numpy as np
    

src = []


# mouse callback handler
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
      link = './result/%s_result%s' % (filename, ext)
      cv2.imwrite(link, result)
      SetGrid(link, size)
    
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
    

    kmeans(size)


def kmeans(size):
    m = 255*3
    map = [0,0,0,0,0]
    answer = list()
    for k in range(size):
        for i in range(5):
        
            im = './obj/img'+str(k)+','+str(i)+'.jpg'
            myimg = cv2.imread(im)
            avg_color_per_row = np.average(myimg, axis=0)
            avg_color = np.average(avg_color_per_row, axis=0)
            map[i] = avg_color[0]+avg_color[1]+avg_color[2]
            #print(map)
            num = 1+map.index(min(map))
        if(num==1):
            print("@ * * * *")
        elif(num==2):
             print("* @ * * *")
        elif(num==3):
            print("* * @ * *")
        elif(num==4):
            print("* * * @ *")
        elif(num==5):
            print("* * * * @")
        else:
             print("* * * * *")
        answer.append(num)
             #print('[',k,']',5-map.index(m))
    print(answer)
# main



img_path = './img/Airplay 2019-12-23 14-38-02-367.jpg'
filename, ext = os.path.splitext(os.path.basename(img_path))
ori_img = cv2.imread(img_path)
size = 13
cv2.namedWindow('img')
cv2.setMouseCallback('img', mouse_handler)

cv2.imshow('img', ori_img)

cv2.waitKey(0)

