'''
Created on 2019. 12. 19.

@author: dswhd
''' 
import cv2
import numpy
m = 255*3
map = [0,0,0,0,0]
for k in range(16):
    for i in range(5):
            
        im = './obj/img'+str(k)+','+str(i)+'.jpg'
        myimg = cv2.imread(im)
        avg_color_per_row = numpy.average(myimg, axis=0)
        avg_color = numpy.average(avg_color_per_row, axis=0)
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
    #print('[',k,']',5-map.index(m))
    