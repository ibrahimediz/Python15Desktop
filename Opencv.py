import cv2
import numpy as np



img = cv2.imread('indir.jpg',cv2.IMREAD_GRAYSCALE)

px = img[50:80,30:55]
print(px)
# print(img.size)
# print(img.shape)
# print(img.dtype)

img[0:30,0:25] = px

img[50:80,30:55] = [1]

# cv2.line(img,(0,0),(150,150),(59,116,249),5)

# cv2.rectangle(img,(15,15),(100,100),(0,0,255),5)

# cv2.circle(img,(60,55),20,(237,136,249),5)

# font = cv2.FONT_HERSHEY_SIMPLEX
# cv2.putText(img,"Vektorel",(0,60),font,2,(237,136,249),3)


cv2.imshow('resim',img)
cv2.waitKey(0)
cv2.destroyAllWindows()