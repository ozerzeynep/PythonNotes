a= 2.4          
print(a)
print(int(a))       #floatı int e dönüştürme işlemi

a=5
print(a)
print(float(a))     #int i floata dönüştürme işlemi

a=11
print(a)
print(str(a))       #int i str çevirme

print("---------------------------------------------------------------")

deger = 20
print(deger)
print(str(deger))
print(type(deger))

##YAPILAN HATALARI##
#a="51a"
#print(int(a))       #string bir ifadedeki harfi int e dönüştüremeyiz

#a=22222558789548
#print(len(a))       #int bir ifadenin uzunluğu bulunamaz

print("Merhaba Dünya",5,4,8,"Hello", sep= "-")      #print ile yazıların arasını ayarlama
print("Zeynep","Özer","Yönetim Bilişim Sistemleri", sep= "**")

print("****************************************")

print("Zeynep Özer","YÖNETİM BİLİŞİM SİSTEMLERİ","3.SINIF ÖĞRENCİSİ","NOT ORTALAMASI: 3.31", sep= "****")

print("Zeynep","Özer","Yönetim Bilişim Sistemleri", end= "..")      #print ile bir yazının sonunu ayarlama
print("Zeynep Özer","YÖNETİM BİLİŞİM SİSTEMLERİ","3.SINIF ÖĞRENCİSİ","NOT ORTALAMASI: 3.31", end= "****")

print(* "TBMM")
print(* "TBMM", sep= ".")       #print ile yazıları ayrı ayrı yazdırma işlemi


print("{} ile {}'ün toplamı : {} sayısına eşittir.".format(5, 4, 9))

print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
print("{a} adlı öğrencimiz, {b} not ortalamasını alarak, {c} üniversitesini birincilikle bitirmiştir" .format(a= "Zeynep Özer", b= 3.90, c= "Bilecik Şeyh Edebali"))

print("{a} ile {b} çarpımı : {c} sayısıdır.".format(a = 6,b = 8,c = 54))


strvar = "Python Öğreniyorum"
print(strvar.upper())       #büyük harfe dönüştürür
print(strvar.lower())       #küçük harfe dönüştürür
print(strvar.split())       #ayırma işlemi yapar



yas1 = 25
yas2 = 19
print(yas1<14)
print(yas1>14)          #Boolean ile ilgili bazı örnekler
print(yas2<yas1)
print(not yas2<yas1)
print(yas1 == yas2)
print(yas1 != yas2)

print("//////////////////////////////////////////////////////////")

ortalaması = 88.7
yuzdelik_dilim = 15
print(yuzdelik_dilim < ortalaması)
print(yuzdelik_dilim >= ortalaması)

###LİSTE VERİ TİPİ
liste = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
print(liste)
print(type(liste))

print(liste.append(16))     #listeye veri ekleme işlemi
print(liste)

print(liste.pop())
print(liste)                #listeden veri çıkartma işlemi yapıldı

print(liste.sort())
print(liste)                #liste küçükten büyüğe sıralandı

print(liste.sort(reverse=True))
print(liste)            #liste büyükten küçüğe sıralandı

print(liste.reverse())
print(liste)        #listeyi terse çevirme işlemi

print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")

ogrenci_listesi = ["Zeynep Özer", "Emine Nur Çalı", "Reyhan Özer", "Zehra Pak", "Esma Arslan", "Firdevs Pak"]
print(ogrenci_listesi)
print(ogrenci_listesi.append("Fatih Pak"))
print(ogrenci_listesi.append("Muteber Pak"))
print(ogrenci_listesi.append("Duru Aydın"))
print(ogrenci_listesi.sort())
print(ogrenci_listesi.sort(reverse=True))
print(ogrenci_listesi.reverse())
print(ogrenci_listesi)


print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")

liste1 = ["Zeynep", "Reyhan", "İlknur"]
liste2 = ["Muteber"]
liste3 = liste1 + liste2        #listeleri toplama işlemi yapıldı
print(liste3)

print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")

listeBir = ["Bilgi İşlem Teknik Servis"]
listeİki = ["Bilgi İşlem Ağ Yönetim Sistemi"]
listeUc = ["Bilgi İşlem Yazılım Sistemleri"]
listelerim = listeBir + listeİki + listeUc
print(listelerim)

print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")

liste4 = [12,25]
liste5 = liste4 * 3
print(liste5)           #listeleri çarpma işlemi yapıldı

liste11 = [11,54,87,96]
liste12 = liste11 + [100]
print(liste12)          #farklı bir yöntemle listeye eleman ekleme yapıldı

ogrenci_listesi = ["Zeynep Özer", "Eylül Tombul", "Asuman Açar", "İlknur Pak Özer", "Reyhan Özer", "Muhteber Pak"]
print(ogrenci_listesi[:3])      #listeden belli bir kısmı çekip alma
print(ogrenci_listesi[::-1])
print(ogrenci_listesi[4:])
print(ogrenci_listesi[::2])
print(ogrenci_listesi[2:6:3])

ortalama = [88,90,55,67,83,25,57,98]
ortalama[2] = 75
print(ortalama)     #listede belli bir elemanı değiştirme

ortalama = [88,90,55,67,83,25,57,98]
ortalama.insert(58,79)      #listeye aynı anda birden fazla eleman eklemek için kullanırı
print(ortalama)

meyve = ["Kivi", "Kavun", "Mandalina"]
meyve.remove("Kavun")       #listeden belli bir elemanı çıkartır
print(meyve)

takım1 = ["Ali", "Kerem", "Asuman", "Seren"]
takım2 = ["Güzide", "Cansu", "Sergen", "Ahmet", "Eren Hakan"]
takım1.extend(takım2)       #bir listeyi başka bir liste ile genişletme/birleştirme işlemi yapıldı
print(takım1)

print("''''''''''''''''''''''''''''''''''''")

ulasım_sekli = ["Otobüs", "Minübüs", "Tren"]
print(ulasım_sekli)
ulasım2 = ["Metro", "Metrobüs", "Hızlı Tren", "Tranvay", "Marmaray", "Uçak", "Gemi"]
ulasım_sekli.extend(ulasım2)
print(ulasım_sekli)

print("'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''")

takım2 = ["Güzide", "Cansu", "Sergen", "Ahmet", "Eren Hakan"]
index = takım2.index("Sergen")
print(index)        #listede belli bir değerin index'ini bulma işlemi


takım1 = ["Ali", "Kerem", "Asuman", "Seren"]
index2 = takım1.index("Ali")
print(index2)

listeler = [1,2,3,3,3,3,5,6,7,8,8,9,3,3,3,5]
count = listeler.count(3)       #listede bir elemanın kaç kere geçtiğini gösterir
print(count)

count2 = listeler.count(8)
print(count2)

value = [1,2,"SLM",True,False,[1,2,3]]
print(value)
print(value.clear())        #listedeki tüm elemanları temizler
print(value)

original_liste = [True, False, 1,2,3,4,5,"Hello World", "SLM", True, [1,2,3,4,False]]
copy_liste = original_liste.copy()      #listeyi kopyalamak için kullanılır
print(copy_liste)

degerler = [87,53,12,0,15,78]
min_value = min(degerler)
max_value = max(degerler)
print(min_value)        #listedeki minimum değeri getirir
print(max_value)        #listedeki maximum değeri getirir

dogru_yanlıs = [True,True, True, True, False]
any_true = any(dogru_yanlıs)
all_true = all(dogru_yanlıs)
print(any_true)     #Herhangi bir True değeri var mı?
print(all_true)     #Bütün hepsi True mu?


urun_stok_miktarı = [150,2876,15,54,3,789,52]
min_urun = min(urun_stok_miktarı)
max_urun = max(urun_stok_miktarı)
print(min_urun)
print(max_urun)

kisi = ["Ali", "Veli", "Ayşe", "Fatma", "Nuriye"]
del kisi[2]                     #silme işlemini 'del' ile yapmış olduk
print(kisi)


print(dir(liste))      #listelerin tüm metodlarını bu şekilde göre biliriz

sube_kisileri = ["Ceren", "Fadime", "Uğur", "Karya"]
print(sube_kisileri.insert(1,"Zeynep"))     #instert ifadesi ile istediğimiz index'e değer ekleriz 
print(sube_kisileri)

len(sube_kisileri)
print(sube_kisileri.insert(len(sube_kisileri),"Seren")) #uzunluğunu bilmetdiğim bir liste olduğunu 
print(sube_kisileri)                                #varsayarsak eğer bu şekilde son kısma istediğim elemanı
                                                    #ekleyebilirim


alan = [30,8,96,78,25,14,520]
print(alan.sort())   #Listeyi küçükten büyüğe sıralar
print(alan)
print(alan.sort(reverse=True))  #Listeyi büyükten küçüğe sıralar
print(alan)




























