import time
class hocalar():

    def __init__(self,ad,soyad,branslar,maili):
        self.ad= ad
        self.soyad= soyad
        self.branslar= branslar
        self.maili= maili

    def hocabilgileri(self):
        print("Bilgiler Yazdırılıyor...")
        time.sleep(1)
        print("""
        Ad : {}
        Soyad : {}
        Branş : {}
        Mail : {}
        """.format(self.ad,self.soyad,self.branslar,self.maili))

    def bransekle(self,yeni_brans):
        print("Branş Ekleniyor...")
        time.sleep(1)
        self.branslar+=yeni_brans
        time.sleep(1)
        print("Branş Eklendi")

hoca1=hocalar("İpek","Sile","İngilizce","sile@itu.edu.tr")
hoca1.bransekle("Makine")

hoca1.hocabilgileri()
