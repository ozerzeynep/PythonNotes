#SET VERİ TİPİ
sayilar = {2,4,8,14}
print(sayilar)
print(type(sayilar))

set1 = {1,2,3}
set2 = {3,4,5}
union_set = set1.union(set2)        #set leri birleştirme işlemi yapılır
print(union_set)

intersection_set = set1.intersection(set2)
print(intersection_set)     #sette kesişimi yani ortak olan değeri bizlere verir

different_set = set1.difference(set2)
print(different_set)        #set veri tipindeki farkı bulur

#TUPLE VERİ TİPİ
#DEĞİŞTİRİLEMEYEN VERİ TİPLERİDİR
tup = ('a','b', 'c')
print(tup)
print(type(tup))

#veriler = ("Ali","Ahmet","Alparslan","Arda","Arif")
#veriler[0] = "Ayşe"
#print(veriler)      #tupplar değiştirilemezlerdir


isimler = ("Zeynep", "Reyhan", "İlknur","Reyhan")
diger = isimler.count("Reyhan")     #bir tuple içerisinde bir değerden kaç tane bulunduğunu bizlere döndürür
print(diger)

print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")

deger = ("DVD Sürücü", "Ram Bellek", "Sabit Disk Sürücü", "İşlemci", "Optik Sürücü", "Ram Bellek", "Ram Bellek")
sistem = deger.count("Ram Bellek")
print(sistem)
sistem2 = deger.index("Ram Bellek")
print(sistem2)
uzunluk = len(deger)
print(uzunluk)
print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")

isimler = ("Zeynep", "Reyhan", "İlknur","Reyhan")
diger2 = isimler.index("İlknur")        #bir tuple içerisinde ki bir değerin konumunu bizlere döndürür
print(diger2)

my_tuple = (1,2,3,4,5,6,7,8,9,14,54,78,98,99,100,54,76,25,23,23,23,21,20)
length = len(my_tuple)      #bir tuple uzunluğunu bizlere döndürür
print(length)


my_tuple2 = (14,54,78,98,99,100,54,76,25,23,23,23,21,20)
sorted_tuple = sorted(my_tuple2)        #tuple içindeki ögeleri sıralama yapar
print(sorted_tuple)

tuplee = (10,50,70)
max_tuple = max(tuplee)
min_tuple = min(tuplee)
print(max_tuple)        #tuple içindeki en büyük değeri döndürür
print(min_tuple)        #tuple içindeki en küçük değeri döndürür

my_tuple3 = (10,20,30,40,50,60,70,80,90,100)
total = sum(my_tuple3)
print(total)


#DICTIONARY VERİ TİPİ
dict1 = {
    'İsim' : 'Zeynep',
    'Soyisim' : 'Özer',
    'Bölümü' : 'Yönetim Bilişim Sistemleri',
    'Yaşı' : 20,
    'Lokasyonu' : 'İstanbul'
    }
print(dict1)
print(type(dict1))

dict2  = {
    'Ogrenci_Numarası' : 25,
    'Ogrenci_Adı_Soyadı' :'Kuzey Kırcıoğlu',
    'Ogrencinin_Bölümü' : 'Yazılım Mühendisliği',
    'Ogrencinin_Yaşı' : 22,
    'Ogrencinin_Lokasyonu' : {
        'Ogrencinin_Doğduğu_Şehir' : 'İstanbul',
        'Ogrencinin_Yaşadığı_Şehir' : 'New York'
        }
    }
print(dict2)
print(dict2['Ogrenci_Numarası'])        #dictionary den istediğimiz veriyi kolayca çeke biliriz
print(dict2['Ogrencinin_Bölümü'])
print(dict2['Ogrencinin_Lokasyonu']['Ogrencinin_Yaşadığı_Şehir'])  
print(dict2.get('Ogrenci_Adı_Soyadı'))      #bu seferde get metodu ile veri çekilmiş oldu

print(dict2.keys())     #anahtarları çekmemizi sağlar
print(dict2.values())   #anahtarlara karşılık gelen değereleri çekmemizi sağlar
print(dict2.items())    #hem anahtarı hem değerini aynı anda almamızı sağlar


stok = {
        'Stok Sahibi Firma' : 'Abalıoğlu Holding',
        'Stok Yeri' : 'Beyoğlu / İstanbul',
        'Stok Gidecek Yerler' : 'Bilecik , Sakarya, Eskişehir, Bursa',
        'Stok Miktarı' : {
            'Kiloya Göre Miktar' : '200 Ton',
            'Adede Göre Miktar' : 800.000
            }
        }
print(stok)
print(stok.keys())
print(stok.values())
print(stok.items())


















