import time
class Yemek():
    def __init__(self):
        pass
    def Pisir(self):
        print("Yemeğiniz Pişiriliyor...")
        time.sleep(0.5)
        print("Yemek Pişirilmiştir.")
        time.sleep(0.5)
        print("Yemek Hazır. Afiyet Olsun :)\n\n")

class Yumurta(Yemek):
    def __init__(self,tereyag_Gram,yumurta_Adet,tuz_Gram):
        print("##### Yumurta Hazırlanıyor #####")
        self.tereyag_Gram = tereyag_Gram
        self.yumurta_Adet = yumurta_Adet
        self.tuz_Gram = tuz_Gram
    def YumurtaKir(self):
        print(f"{self.yumurta_Adet} adet yumurta kırılmıştır.")
        time.sleep(0.5)
    def TuzEkle(self):
        print(f"{self.tuz_Gram} gram tuz eklenmiştir.")
        time.sleep(0.5)
    def TereyagEkle(self):
        print(f"{self.tereyag_Gram} gram tereyağ eklenmiştir.")
        time.sleep(0.5)
        
class Pilav(Yemek):
    def __init__(self,pirinc_SuBardagi,sicakSu_SuBardagi,tereyag_Gram,tuz_Gram):
        print("##### Pilav Hazırlanıyor #####")
        self.pirinc_SuBardagi = pirinc_SuBardagi
        self.sicakSu_SuBardagi = sicakSu_SuBardagi
        self.tereyag_Gram = tereyag_Gram
        self.tuz_Gram = tuz_Gram
    def PirincEkle(self):
        print(f"{self.pirinc_SuBardagi} su bardağı pirinç eklenmiştir.")
        time.sleep(0.5)
    def SicakSuEkle(self):
        print(f"{self.sicakSu_SuBardagi} su bardağı sıcak su eklenmiştir.")
        time.sleep(0.5)
    def TuzEkle(self):
        print(f"{self.tuz_Gram} gram tuz eklenmiştir.")
        time.sleep(0.5)
    def TereyagEkle(self):
        print(f"{self.tereyag_Gram} gram tereyağ eklenmiştir.")
        time.sleep(0.5)

class PatatesliTavuk(Yemek):
    def __init__(self,tavuk_Adet,patates_Adet,sarimsak_Adet,biberSalcasi_YemekKasigi,zeytinYagi_CayBardagi,tuz_Gram):
        print("##### Patatesli Tavuk Hazırlanıyor #####")
        self.tavuk_Adet= tavuk_Adet
        self.patates_Adet= patates_Adet
        self.sarimsak_Adet= sarimsak_Adet
        self.biberSalcasi_YemekKasigi= biberSalcasi_YemekKasigi
        self.zeytinYagi_CayBardagi= zeytinYagi_CayBardagi
        self.tuz_Gram= tuz_Gram
    def TuzEkle(self):
        print(f"{self.tuz_Gram} gram tuz eklenmiştir.")
        time.sleep(0.5)
    def PatatesEkle(self):
        print(f"{self.patates_Adet} adet patates eklenmiştir.")
        time.sleep(0.5)
    def TavukEkle(self):
        print(f"{self.tavuk_Adet} adet tavuk eklenmiştir.")
        time.sleep(0.5)
    def SarimsakEkle(self):
        print(f"{self.sarimsak_Adet} adet sarımsak eklenmiştir.")
        time.sleep(0.5)
    def BiberSalcasiEkle(self):
        print(f"{self.biberSalcasi_YemekKasigi} yemek kaşığı biber salçası eklenmiştir.")
        time.sleep(0.5)
    def ZeytinYagiEkle(self):
        print(f"{self.zeytinYagi_CayBardagi} çay bardağı zeytin yağı eklenmiştir.")
        time.sleep(0.5)

yumurta = Yumurta(20,2,5)
yumurta.TereyagEkle()
yumurta.YumurtaKir()
yumurta.TuzEkle()
yumurta.Pisir()

time.sleep(2)

pilav = Pilav(2,2.5,20,5)
pilav.TereyagEkle()
pilav.PirincEkle()
pilav.SicakSuEkle()
pilav.TuzEkle()
pilav.Pisir()

time.sleep(2)

tavuk = PatatesliTavuk(1,4,3,1,0.5,5)
tavuk.ZeytinYagiEkle()
tavuk.BiberSalcasiEkle()
tavuk.TavukEkle()
tavuk.PatatesEkle()
tavuk.SarimsakEkle()
tavuk.TuzEkle()
tavuk.Pisir()
