import cv2
import numpy as np

negx= cv2.imread("negx.jpg")
negy= cv2.imread("negy.jpg")
negz= cv2.imread("negz.jpg")
posx= cv2.imread("posx.jpg")
posy= cv2.imread("posy.jpg")
posz= cv2.imread("posz.jpg")

negx=cv2.resize(negx,(200,200))
negy=cv2.resize(negy,(200,200))
negz= cv2.resize(negz,(200,200))
posx= cv2.resize(posx,(200,200))
posy= cv2.resize(posy,(200,200))
posz= cv2.resize(posz,(200,200))

#negx= cv2.copyMakeBorder(negx,top,bot,left,right,cv2.BORDER_CONSTANT,value=0)
negx= cv2.copyMakeBorder(negx,200,200,0,0,cv2.BORDER_CONSTANT,value=0)
posx= cv2.copyMakeBorder(posx,200,200,0,0,cv2.BORDER_CONSTANT,value=0)
negz= cv2.copyMakeBorder(negz,200,200,0,0,cv2.BORDER_CONSTANT,value=0)

new=cv2.vconcat([posy,posz,negy])
new=cv2.hconcat([negx,new,posx,negz])


#cv2.imshow("a",negx)
cv2.imshow("cube map",new)
cv2.imwrite("cubemap.png", new)
cv2.waitKey(0)
