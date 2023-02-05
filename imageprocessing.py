import cv2
import numpy as np
cam = cv2.VideoCapture(1)
cv2.namedWindow("Capture Imgae")
img_counter = 0
while True:
 ret,frame = cam.read()
 
 if not ret :
 print("failed to capture")
 break 
 
 cv2.imshow("frames",frame)
 
 k = cv2.waitKey(1)
 
 # if k == ord("q"):
 # break 
 
 if k == ord("c"):
 
Page 67 of 74
 
 cv2.imwrite('E:\\Project\\img_name_{}.png',frame)
 
 img_counter+=1
 
 
 break 
cam.release()
 
 
img = cv2.imread("E:\\Project\\img_name_{}.png",0)
img = cv2.resize(img,(500,500))
cv2.imshow("orignal",img)
_,th1 = cv2.threshold(img,50,255,cv2.THRESH_BINARY)
_,th2 = cv2.threshold(img,50,255,cv2.THRESH_BINARY_INV)
_,th3 = cv2.threshold(img,127,255,cv2.THRESH_TRUNC)
_,th4 = cv2.threshold(img,100,255,cv2.THRESH_TOZERO)
cv2.imshow("1-Thresh Binary",th1)
cv2.imshow("2-Thresh Binary Inv",th2)
cv2.imshow("3-Thresh Trunc",th3)
cv2.imshow("4-Thresh Towards zero",th4)
_,th5 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
 
Page 68 of 74
th6 = 
cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,9)
th7 = 
cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,1
1)
cv2.imshow("original",img) 
cv2.imshow("Thresh Binary",th1)
cv2.imshow("Adaptive 1",th2)
cv2.imshow("Adaptive 2",th3)
_,mask = cv2.threshold(img,165,255,cv2.THRESH_BINARY_INV)
kernel = np.ones((3,3),np.uint8)
e = cv2.erode(mask,kernel)
cv2.imshow("Orignal",img)
cv2.imshow("mask",mask)
#cv2.imshow("kernel",kernel)
cv2.imshow("Erosion",e)
kernel = np.ones((3,3),np.uint8)
d = cv2.dilate(mask,kernel)
cv2.imshow("Dilation",d)
_,mask = cv2.threshold(img,165,255,cv2.THRESH_BINARY_INV)
kernel = np.ones((3,3),np.uint8)
 
Page 69 of 74
o = cv2.morphologyEx(mask,cv2.MORPH_OPEN,kernel)
cv2.imshow("Orignal",img)
cv2.imshow("mask",mask)
#cv2.imshow("kernel",kernel)
cv2.imshow("Opening",o)
kernel = np.ones((3,3),np.uint8)
c = cv2.morphologyEx(mask,cv2.MORPH_CLOSE,kernel)
cv2.imshow("Closing",c)
x1 = cv2.morphologyEx(mask,cv2.MORPH_TOPHAT,kernel) #Dif/B mask and opening 
x2 = cv2.morphologyEx(mask,cv2.MORPH_GRADIENT,kernel) #Dif/B Dilation And Erosion
x3 = cv2.morphologyEx(mask,cv2.MORPH_BLACKHAT,kernel)
cv2.imshow("x1",x1)
cv2.imshow("x2",x2)
cv2.imshow("x3",x3)
cv2.imwrite("E:\\Project\\Micro photos\\original.JPG",img)
cv2.imwrite("E:\\Project\\Micro photos\\th1.JPG",th1)
cv2.imwrite("E:\\Project\\Micro photos\\th2.JPG",th2)
cv2.imwrite("E:\\Project\\Micro photos\\th3.JPG",th3)
cv2.imwrite("E:\\Project\\Micro photos\\th4.JPG",th4)
 
Page 70 of 74
cv2.imwrite("E:\\Project\\Micro photos\\th5.JPG",th5)
cv2.imwrite("E:\\Project\\Micro photos\\Adp th6.JPG",th6)
cv2.imwrite("E:\\Project\\Micro photos\\Adp th7.JPG",th7)
cv2.imwrite("E:\\Project\\Micro photos\\Mask.JPG",mask)
cv2.imwrite("E:\\Project\\Micro photos\\Erosion.JPG",e)
cv2.imwrite("E:\\Project\\Micro photos\\Dilation.JPG",d)
cv2.imwrite("E:\\Project\\Micro photos\\Morphology Tophat.JPG",x1)
cv2.imwrite("E:\\Project\\Micro photos\\Morphology Gradient.JPG",x2)
cv2.imwrite("E:\\Project\\Micro photos\\Morphology Blackhat.JPG",x3)
cv2.waitKey()
cv2.destroyAllWindows()
