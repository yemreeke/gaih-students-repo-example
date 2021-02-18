notlar =list()
ogrenciler = list()
bilgi = dict()
adet = 5
for i in range(adet):
    print(f"Öğrenci {i+1} bilgilerini giriniz.")
    notlar.append(list())
    ogrenciler.append(list())
    ogrenciler[i].append(input("Ad Giriniz:"))
    ogrenciler[i].append(input("Soyad Giriniz:"))
    notlar[i].append(int(input("Vize Notu Giriniz:")))
    notlar[i].append(int(input("Final Notu Giriniz:")))
    notlar[i].append(int(input("Ev Ödevi Notu Giriniz:")))
    print()
for i in range(adet):
    bilgi[f"Öğrenci {i+1}"]={"Ad":ogrenciler[i][0],"Soyad":ogrenciler[i][1],"Vize":notlar[i][0],"Final":notlar[i][1],"Ev Ödevi":notlar[i][2]}
for i in range(adet):
    notlar[i].append((notlar[i][0]+notlar[i][1]+notlar[i][2])/3)
enBuyuk = notlar[0][3]
for i in range(adet):
    if(enBuyuk<notlar[i][3]):
        enBuyuk=notlar[i][3]
        indis = i
print(f"Tebrikler {ogrenciler[indis][0]} {ogrenciler[indis][1]} , {enBuyuk} Ortalama İle Sınıf 1.si Oldunuz :)")
