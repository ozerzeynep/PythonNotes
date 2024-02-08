print("Zeynep")
print("Hello World")
print("Hello \nWorld")      #bir alt satıra geçiş yapmasını sağlar
print("Hello \tWorld")      #tab boşluğu oluşturmasını sağlar
print("Benim Adım {}, Yaşım {}".format('Zeynep', '20'))   #Format komutu kullanılarak boşluk doldurma yapıldı.
print("İsimi {}, Soyisim {}, Yaşı {}'dır.".format('Zeynep', 'Özer', 20))
print("İsim {ad}, yaşı {yas}".format(ad= 'Zeynep', yas= 20))  #parantez içiresine değişken ismi verip işlem yapmak daha sağlıklıdır.


#SAYISAL DEĞERLER
sayi=10
print(sayi)

a=5
b=4
print(a*b)
print(a+b)
print(a/b)
print(a-b)
print(a//b)     #değerlerin int şeklinde çıkmasını sağlar
print(a%b)      #mod alma yapılır
print(a**b)     #küp alma yapılır

a=18
b=11
c=4
print(a*c//b)

sayi= 11
sayi= sayi + 5      #kodlar sağdan sola doğru okunmaktadır
print(sayi)

print("-----------------------------------------------------")

sayi1 = 152
sayi1 = sayi1 * 3
print(sayi1)


a= "Zeynep Özer"
print(a[0:8])       #belli bir değer aralığında alınmasını sağlar
print(a[2])         #bilgisayar dilinde sayma sayıları 0 dan başlar
print(a[::-1])      #ifadenin tersten yazılmasını sağlar
print(a[::2])       #ikişer ikişer gitmesini sağlar
print(a[1:10:3])    #burda birden başla ona kadar git ve üçer üçer atlayarak git anlamına gelir
print(a[-1])        #son değerin alınmasını sağlar

print("------------------------------------------------------------------------------")

deger_aralıgı = "İlknur Pak Özer"
print(deger_aralıgı[4:])
print(deger_aralıgı[0:8:2])
print(deger_aralıgı[::-1])
print(len(deger_aralıgı))



deger= "Türkiye Büyük Millet Meclisi"
print(len(deger))       #uzunluk bulmayı sağlar(boşluklarda sayılmaktadır)


#VERİ TİPLERİ
#INTEGER-int-tam sayı yapılmasını sağlar
#FLOAT-float-ondalıklı sayılardır
#STRING-str-metinsel ifadelerdir
#BOOLEAN-bool-mantıksal ifadelerdir
#LIST-list-birçok veriyi içinde barındırır/köşeli parantezle ifade edilir
#SET-set-birçok veriyi içinde barındırır ancak aynı veriler olamaz/kıvırcık parantezle ifade edilir
#DICTIONARY-dict-key values şeklinde değerleri tutar/kıvırcık parantezle ifade edilir
#TUPLE-tup-listeye benzer / ancak tuplelar değiştirilemezler/normal parantezle ifade edilir

a="HTML"
b="CSS"             #string ifadeleri bu şekilde toplayabiliriz
c="JAVASCRIPT"
print(a+b+c)

a="HTML-CSS"
print(a*3)          #string ifadeyi çarpa işlemi

#NOTLAR:
#DEĞİŞKEN İSİMLERİ SAYI İLE BAŞLAMAZ
#DEĞİKEN İSİMLERİNDE BOŞLUK BIRAKILMAZ
#DEĞİŞKEN İSİMLERİNDE ÖZEL KARAKTERLER BULUNDURULMAZ(ALT ÇİZGİ HARİÇ)
#BİR DEĞİŞKENE İKİ YADA DAHA FAZLA DEĞER ATANABİLİR HER ZAMAN SON DEĞER GEÇERLİ OLACAKTIR

a=b=c=10
print(a*b*c)

x=20
x=55
x=28
print(x)

x,y,z = 11,20,5
print(z)
print(z**x//y)


x,y,z = 11,20,5
x,y,z = z,x,y       #değişken takası yapılmış oldu
print(z**x//y)
print(z)


str(15)             #stringe dönüştürme
print(str(15))

print(int(1.15))
print(int(11.2))        #inte dönüştürme


print(float(5))         #floata dönüştürme yapılır


#NOT:BİR INTEGER İLE BİR STRING İFADE TOPLANMAZ
#print("9"+999)      #bu ifade hata vericektir

print(len("türkiye"))       #string bir ifadenin uzunluğunu bize döndürür
print(len("Zeynep Özer"))
print(len("İlknur Pak Özer"))

print(type(5))  #türü bize verir
print(type("Kuzey"))
print(type(True))
print(type(5.14))
print(type([True,1,1.5,"Merhaba Dünya"]))
print(type({True,1}))
















