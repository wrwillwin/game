import cv2
import os
img=cv2.imread(r'h.jpg')
filename=0
filenum=0
img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
b=20#数字块大小为20×20
m=img.shape[0]//b
n=img.shape[1]//b
print(m,n)
for i in range(m):
    offsetRow=i*b
    if i%5==0 and i !=0:
        filename+=1
        filenum=0
    path="D:\\python_code"+str(filename)
    if not os.path.exists(path):
        os.makedirs(path)
    for j in range(n):
        offsetCol=j*b
        filepath=path+"\\"+str(filenum)+".jpg"
        filenum+=1
        im=img[offsetRow:offsetRow+b-1,offsetCol:offsetCol+b-1]
        cv2.imwrite(filepath,im, [int( cv2.IMWRITE_JPEG_QUALITY), 95])
#print(filename,filenum)
#print(path)
