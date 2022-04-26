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

cv2.waitKey(0)
cv2.destroyAllWindows()
