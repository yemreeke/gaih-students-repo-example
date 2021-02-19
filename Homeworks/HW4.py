class HangmanOyunu():
    def __init__(self,name):
        self.name=name
        self.tahmin=""
    def KelimeBelirle(self,kelime):
        self.kelime=kelime.upper()
    def HakBelirle(self,hak):
        self.hak=hak
    def Baslat(self):
        try:
            str(self.kelime)+str(self.hak)
        except:
            print("Hak ve Kelime belirlemeniz lazım.")
            return
        print(f"Oyunumuza Hoşgeldin {self.name}")
        while(self.hak>=0):
            print()
            bosYer=0
            for harf in self.kelime:
                if(harf in self.tahmin):
                    print(harf,end=" ")
                else:
                    print("_",end=" ")
                    bosYer+=1
            print()
            if(bosYer==0):
                print("Tebrikler Kazandınız!")
                return
            if(self.hak==0):
                break
            h = input("Harf Giriniz:").upper()
            self.tahmin+=h
            if(h not in self.kelime):
                print("Harf Yoktur!")
            else:
                print("Harf Vardır.")
            self.hak-=1
            print(f"{self.hak} hakkınız kalmıştır.")      
        print("\nKaybettiniz!")

#Test
#oyun = HangmanOyunu("Emre")
#oyun.Baslat()

oyun = HangmanOyunu("Emre")
oyun.KelimeBelirle("python")
oyun.HakBelirle(10)
oyun.Baslat()
