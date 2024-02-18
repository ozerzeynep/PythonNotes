#FOR DÖNGÜSÜ
sınıflar =["Naz Demir", "İlker Yalın", "Turhan Kayagil"]
for ogrenciler in sınıflar:
    print(ogrenciler)


sınıf = ['Naz Demir', 'İlker Yalın', 'Turhan Kayagil', 'Can Umut']
ogrenci_sayısı = 0
for ogrenci in sınıf:
    ogrenci_sayısı += 1
    print(ogrenci_sayısı,ogrenci)


sınıf2 = ['Naz Demir', 'İlker Yalın', 'Turhan Kayagil', 'Can Umut', 'İlknur Pak Özer', 'Rezzan Timur', 'Seren Çem']
ogrenci_sayısı2 = 0
for ogrenci2 in sınıf2:
    ogrenci_sayısı2 -= 1
    print(ogrenci_sayısı2, ogrenci2)


print("---------------------------------------------------------------------------------------------")


sınıf = ['Naz Demir', 'İlker Yalın', 'Turhan Kayagil', 'Can Umut']
ogrenci_sayısı = 0
for ogrenci in sınıf:
    ogrenci_sayısı += 1
    ad,soyad = ogrenci.split()[0], ogrenci.split()[1]
    print("{0}. Öğrencinin Adı {1} Soyadı {2}".format(ogrenci_sayısı, ad, soyad))
    
  
print("---------------------------------------------------------------------------------------------")    
  
sınıf2 = ['Naz Demir', 'İlker Yalın', 'Turhan Kayagil', 'Can Umut', 'İlknur Pak Özer', 'Rezzan Timur', 'Seren Çem']
ogrenci_sayısı2 = 0
for ogrenci in sınıf2:
    ogrenci_sayısı2 += 1
    ad,soyad = ogrenci.split()[0], ogrenci.split()[1]
    print("{0} Nolu Öğrencinin Adı {1} Soyadı {2}".format(ogrenci_sayısı2, ad, soyad))
    
print("---------------------------------------------------------------------------------------------")

sınıf = ['Naz Demir', 'İlker Yalın', 'Can Umut', 'Turhan Kayagil']
baskan = "Can Umut"
ogrenci_sayısı = 0
baskan_sayısı = 0
for ogrenci in sınıf:
    ad,soyad = ogrenci.split()[0], ogrenci.split()[1]
    if (ogrenci == baskan):
        baskan_sayısı += 1
        print("{0} Nolu Başkanın Adı {1} Soyadı {2}".format(baskan_sayısı, ad, soyad))
    else:
        ogrenci_sayısı += 1
        print("{0} Nolu Öğrencinin Adı {1} Soyadı {2}".format(ogrenci_sayısı, ad, soyad))
    


tup1 = (1,2,3,4,5,6,7,8,9,10,11)
for sayi in tup1:
    print(sayi)

print("---------------------------------------------------------------------------------------------")

liste = [[1,2],[3,4]]
for sayi1,sayi2 in liste:
    print(sayi1)

print("---------------------------------------------------------------------------------------------")


liste = [[1,2],[3,4]]
for sayi1,sayi2 in liste:
    print(sayi2)


liste = [[1,2],[3,4]]
for sayi1,sayi2 in liste:
    print(sayi1,sayi2)


print("---------------------------------------------------------------------------------------------")


liste = [[1,2],[3,4]]
for sayi1,sayi2 in liste:
    print(sayi1*sayi2)
    

#MAAŞLARA %20 ZAM YAPILACAKTIR GEREKLİ KODALIR YAZINIZ

maaslar = [20.000,40.000,50.000,60.000]

def yeni_maas(x):
    print(x*20/100 + x)

for i in maaslar:
    yeni_maas(i)


maaslar1 = [10.000,20.000,30.000,40.000,50.000,60.000,70.000,80.000,90.000]

def ust_sınır(x):
    print(x*10/100 + x)

def alt_sınır(x):
    print(x*20/100 + x)

for i in maaslar1:
    if i >= 30.000:
        ust_sınır(i)
    
    else:
        alt_sınır(i)


print("-----------------------------------------------------")

sınıf_mevcudu = ["Ece Dönmez", "Ali Cenk", "Atakan Gelgör", "Cemre Altın", "Sude Okan"]

for i in sınıf_mevcudu:
    if sınıf_mevcudu == "Merve Akın":
        print("Merve Akın bu sınıftadır.")
    
    else:
        print("Merve Akın bu sınıfta değildir.")
        sınıf_mevcudu.append("Merve Akın")
        print("Merve Akın sınıfa eklendi".format(sınıf_mevcudu))
        break
print(sınıf_mevcudu)
    





