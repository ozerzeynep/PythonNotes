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
    





