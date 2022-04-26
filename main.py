import cv2

import numpy as np

ilkresim = cv2.imread("lena-std.tif")


#cv2.imshow("deneme",ilkresim)
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

#efekt ekleme

#ilkresim[:,:,0]=255# blue özelliğini 255 yaptık
#: : derken resmin tüm her tarafına efekti uygula diyoruz 3. paremetre
# hangi katmanı seçtiğimiz 0 blue, 1 green, 2 red olacak şekilde
# belirli bir alana efekt

#ilkresim[200:300,200:300,0] = 255 #x, y değer aralıları verip ilerliyoruz

#cv2.imshow("blue 255",ilkresim)

# belirli bir bölümü almak istiyoruz resim içinden yeni kesit alıyoruz

kesitresim = ilkresim[50:150,300:400] #y, x kordinatları

#kesiti istediğimiz bir kısma yapıştırma
#ilkresim[0:100,0:100]=kesitresim
#cv2.imshow("kesit",ilkresim)
#print(ilkresim.shape[0]) # 012 şeklinde değerlere ayrı ayrı
# erişebiliyouz uzunluk genişlik ve renk durumu

#aynalama

aynalama = cv2.copyMakeBorder(ilkresim,75,75,100,125,cv2.BORDER_REFLECT)

#uzatma

uzatma = cv2.copyMakeBorder(ilkresim,25,25,25,25,cv2.BORDER_REPLICATE)
#cv2.imshow("aynali",uzatma)

#grileştirme

gri= cv2.cvtColor(ilkresim,cv2.COLOR_BGR2GRAY)#GRİLEŞTİ
# boyutların özellikleri alma
yukseklik,genislik,kanalsayisi = ilkresim.shape
yukseklikg,genislikg = gri.shape
#print("yükseklik: "+ str(yukseklikg)+" genislik: "+str(genislikg))
#cv2.imshow("gri",gri)

#görüntü piramitleri

ikikatbuyuk = cv2.pyrUp(ilkresim)#boyutları 2 katına çıkarıyor

ikikatkucuk = cv2.pyrDown(ilkresim)
#cv2.imshow("kucuk",ikikatkucuk)
#cv2.imshow("orijinal",ilkresim)
#cv2.imshow("iki kat",ikikat)

#numpy kullanma zeros fonskiyonu

resim = np.zeros((300,300,3),dtype="uint8")#kendi resmimizi oluşturduk
#zeros fonskiyonu tüm kapsamları 0 yapıyor her pikseli 0 yapıyor.
#ilk parametresi shape boyut veriyoruz diğeri de data type

#print(resim)
# mean filter kullanımı 
cv2.imshow("orijinal resim",ilkresim)

meanfilter = cv2.blur(ilkresim,(5,5))

cv2.imshow("3x3 mean filter",meanfilter)
cv2.waitKey(0)
cv2.destroyAllWindows()
