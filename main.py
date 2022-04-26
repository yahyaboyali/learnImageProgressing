import cv2

import numpy as np

ilkresim = cv2.imread("lena-std.tif")


cv2.imshow("deneme",ilkresim)
#print(ilkresim) matris karşılığıı böyle alıyoruz

#resmin boyutunu öğrenme

#print(ilkresim.size) ile boyutunu öğreniyoruz

#data tipi ne nasıl öğreniriz

#print(ilkresim.dtype)

#print(ilkresim.shape) #genişliğini ve yüksekliğini aldık

#resmin belirli kısmındaki bgr değerlerini öğrenmek istersek

#print(ilkresim[(230,80)])#230 a 80 deki bgr değerini alıyor

#print("resmin boyutu: "+ str(ilkresim.size))
#print("resmin özellikleri: "+ str(ilkresim.shape))

#print("resmin veri tipi: "+ str(ilkresim.dtype))

# pixel renk değiştirme

#ilkresim[112,45] = [255,255,255]
#for i in range(100): # çizgi çizdi i boyunca
 #   ilkresim[70,i]=[255,255,255]
cv2.imshow("pixel degisti",ilkresim)
cv2.waitKey(0)
cv2.destroyAllWindows()
