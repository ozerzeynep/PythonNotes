#FONKSİYONLAR
#karmaşık işlemleri bir araya toplayarak, bu işlemleri tek adımda yapmamızı sağlamaktadır

def bes_bastir():
    print(5)

bes_bastir()

def bes_dondur():
    return 5

bes_dondur()

def sayi_dondur(sayi):
    print(sayi)

sayi_dondur(15)

def sayi_olustur(sayii = 250):
    print(sayii)

sayi_olustur()
sayi_olustur(18)

def buyuk_sayi_dondur(a,b):
    if a > b:
        print(a)
    elif b > a:
        print(b)
    
buyuk_sayi_dondur(5,10)


def kucuk_sayi_bul(a,b,c):
    if a > b and a > c:
        print(a)
    elif b > a and b > c:
        print(b)
    elif c > a and c > b:
        print(c)

kucuk_sayi_bul(20, 12, 30)

#Kare alma işlemi
def kare_al(x):
    print(x**2)

kare_al(6)

#Çarpma işlemi
def carpim(x,y):
    print(x*y)

carpim(8,9)

#Toplama işlemi (ön tanımlı değer ile yapımı)
def topla(x,y = 1):
    print(x+y)

topla(8)
topla(11+8)

#Isı nem ve sarj hesaplama işlemi
def hesapla(ısı,nem,sarj):
    print((ısı+nem)/sarj)

hesapla(20,40,13)

#Eleman ekleme işlemi
x = []

def eleman_ekle(y):
    x.append(y)
    print(str(y)  + " ifadesi eklendi")

eleman_ekle("Ayhan")
print(x)

#Elemanın türüne bakma
def selamla():
    print("Merhaba")
    print("Nasılsınız?")

print(type(selamla))


#Parametre alarak yapılması
def selamla(isim):
    print("İsminiz :", isim)

selamla("Zeynep")

#Toplama işlemi 
def toplama(a,b,c):
    print("Toplamları", a+b+c)

toplama(25,140,56)

#Faktoriyel hesaplama işlemi
def faktoriyel(sayi):
    faktoriyel = 1
    if(sayi == 0 or sayi == 1):
        print("Faktoriyel :", faktoriyel)
    else:
        while(sayi >= 1):
            faktoriyel *= sayi
            sayi -= 1
        print("Faktoriyel :", faktoriyel)

faktoriyel(1)
faktoriyel(0)
faktoriyel(5)



#Return ile toplama işlemi
def toplamaa(a,b,c):
    print("Bu işlem gerçekleştirildi")
    return a+b+c

print(toplamaa(5,8,9))


def toplamaa(a,b,c):
    return a+b+c
    print("Bu işlem gerçekleştirildi")  #return ifadesinden sonra yazılan hiçbir ifade çalışmayacaktır

print(toplamaa(5,8,9))


#Esnek sayılı parametre oluşturma
def Toplamaa(*a):
    toplam = 0
    for i in a:
        toplam += 1
    print(toplam)

print(Toplamaa(4,5,7,9)) 


 #Global ve Yerel Değişkenler

b = 5       #Global değişken örneğidir
def fonksiyon():
    print(b)
fonksiyon()
print(b)


def fonksiyon():
    a = 10      #Yerel değişken örneği
    print(a)
fonksiyon()


c = 15  #Global değişken
def fonksiyon():
    c = 2  #Yerel değişken
    print(c)
fonksiyon()
print(c)


e = 20
def fonksiyon():
    global e  #Bu ifade benim şimdi sana tanıtacağım ifadeyi kullan demektir
    e = 11
    print(e)
fonksiyon()
print(e) 

 #Lambda kullanımları

def ikiylecarp(x):
    return x * 2        #fonksiyon ile kullanımı
print((ikiylecarp(8)))


ikiylecarp = lambda x : x *2        #lambda ile kullanımı
print(ikiylecarp(10))


def toplama(x,y,z):
    return x + y + z  #fonksiyon ile kullanımı
print(toplama(20,30,40))


toplama = lambda x,y,z : x + y + z  #lambda ile kullanımı
print(toplama(11,25,33))


def terscevir(s):
    return s[::-1]      #fonksiyon ile kullanımı
print(terscevir("Python Programlama"))


terscevir = lambda s: s[::-1]  #lambda ile kullanımı
print(terscevir("Python Öğreniyorum"))


def cifttek(sayi):
    return sayi % 2 == 0  #fonksiyon ile kullanımı
print(cifttek(14))


cifttek = lambda sayi : sayi % 2 == 0  #lambda ile kullanımı
print(cifttek(23)) 



#ÖRNEK: BİR SAYININ ASAL OLUP OLMADIĞINI BULAN BİR FONKSİYON YAZ. EN KÜÇÜK ASAL SAYI 2'DİR.

def asal_mi(sayi):
    if(sayi == 1): 
        return False
    
    elif(sayi == 2):
        return True
    
    else:
        for i in range(2,sayi):
            if(sayi % i == 0):
                return False
        return True
    
while True:
    sayi = input("Sayi :")

    if (sayi == "q"):
        break

    else:
        sayi = int(sayi)
        if(asal_mi(sayi)):
            print(sayi,"asal bir sayıdır.")
        
        else:
            print(sayi,"asal bir sayı değildir.")



#BİR SAYININ TAM BÖLENLERİNİ BULMA İŞLEMİ

def tambolenlerinibul(sayi):
    tam_bolenler = []

    for i in range(2,sayi):
        if(sayi % i == 0):
            tam_bolenler.append(i)
    
    return tam_bolenler

while True:
    sayi = input("Sayı :")
    if(sayi == "q"):
        print("Program Sonlandırılıyor")
        break

    else:
        sayi = int(sayi)
        print("Tam Bölenler :",tambolenlerinibul(sayi)) 


 #1'DEN 1000'E KADAR OLAN SAYILARDAN MÜKEMMEL SAYI PARÇALARINI EKRANA YAZDIRIN. BUNUN İÇİN BİR SAYININ MÜKEMMEL OLUP OLMADIĞINI DÖNEN BİR FONKSİYON YAZDIRIN. MÜKEMMEL SAYI BİR SAYINNI BÖLENLERİNİN KENDİSİNE EŞİT OLMASIDIR.

def mukemmel(sayi):
    toplam = 0

    for i in range(1,sayi):
        if(sayi % i == 0):
            toplam += i
    return toplam == sayi

for i in range(1,1001):
    if(mukemmel(i)):
        print("Mükemmel Sayı :",i) 


 #KULLANICIDAN 2 ADET SAYI ALARAK BU LİSTENİN EN BÜYÜK ORTAK BÖLENİ(EBOB) DÖNEN BİR TANE FONKSİYON YAZINIZ.

def ebob_bul(sayi1,sayi2):
    i = 1
    ebob = 1

    while(i <= sayi1 and i <= sayi2):
        if(not (sayi1 % i) and not(sayi2 % i)):
            ebob = i
        i += 1
    return ebob

sayi1 = int(input("Sayı-1:"))
sayi2 = int(input("Sayı-2:"))

print("Ebob :",ebob_bul(sayi1,sayi2)) 



 #KULLANICIDAN İKİ ADET SAYI ALARAK BU SAYILARIN EN KÜÇÜK ORTAK KADLARINI(EKOK) BULAN FONKSİYONU YAZINIZ.

def ekok_bulma(sayı1,sayı2):
    
    i = 2
    ekok = 1
    while True:
        if (sayı1 % i == 0 and sayı2 % i == 0):
            ekok *= i

            sayı1 //= i
            sayı2 //= i


        elif (sayı1 % i ==  0 and sayı2 % i != 0):
            ekok *= i

            sayı1 //= i


        elif (sayı1 % i != 0 and sayı2 % i == 0):
            ekok *= i

            sayı2 //= i
        else:
            i += 1
        if (sayı1 == 1 and sayı2 == 1):
            break
    return ekok

sayı1 = int(input("Sayı-1:"))
sayı2 = int(input("Sayı-2:"))

print("Ekok:",ekok_bulma(sayı1,sayı2))



#1'DEN 100'E KADAR OLAN SAYILARDAN PİSAGOR ÜÇGENİ OLUŞTURANLARI EKRANA BASAN BİR FONKSİYON YAZIN.

def pisagor_bulma():

    pisagorListesi = list()
    for i in range(1,101):
        for j in range(1,101):

            c = (i ** 2 + j ** 2) ** 0.5

            if(c == int(c)):
                pisagorListesi.append((i,j,int(c)))
    
    return pisagorListesi

for i in pisagor_bulma():
    print(i)



