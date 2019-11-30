import cv2
import numpy as np



img = cv2.imread('bookpage.jpg')

# px = img[50:80,30:55]
# print(px)
# print(img.size)
# print(img.shape)
# print(img.dtype)
 

# cv2.line(img,(0,0),(150,150),(59,116,249),5)

# cv2.rectangle(img,(15,15),(100,100),(0,0,255),5)

# cv2.circle(img,(60,55),20,(237,136,249),5)

# font = cv2.FONT_HERSHEY_SIMPLEX
# cv2.putText(img,"Vektorel",(0,60),font,2,(237,136,249),3)

grayscaled = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
px = grayscaled[0:50,0:50]
print(px)
th = cv2.adaptiveThreshold(grayscaled,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,115,1)
# retval ,treshold = cv2.threshold(grayscaled,20,255,cv2.THRESH_BINARY)

cv2.imshow('resim',img)
cv2.imshow('eşikleme',th)
cv2.waitKey(0)
cv2.destroyAllWindows()