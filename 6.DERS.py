#WHILE DÖNGÜSÜ
#Koşul sağladığı sürece çalış anlamına gelir.
x = 0
while (x<10):
    print(x)
    x += 1
    
y = 0
while y<10:
    print("{} değeri 10'dan küçüktür",format(y))
    y += 1
else:
    print("{} değeri 10'dan büyüktür",format(y))
    

sayi = 6
sonuc = 1
while sayi > 0:
    sonuc = sonuc * sayi        #FAKTÖRİYEL HESAPLAMA İŞLEMİ
    sayi -= 1
print(sonuc)


sayac = 0
while sayac < 5:
    print("Sayaç",sayac)
    sayac += 1
    
sayi1 = 1
while sayi1 <= 10:
    print(sayi1)
    sayi1 += 1
    

toplam = 0
sayac1 = 1
while sayac1 <= 10:
    toplam += sayac1
    sayac1 += sayac1
print("Toplam",toplam)


liste = [1,2,3,4,5,6,7,8,9,10,11]
index = 0
while index < len(liste):
    print("Eleman:",liste[index])
    index += 1


a = 0
while a < 40:
    print("Python Öğreniyorum")
    a += 1
    
    

#While döngüsünün en basit hali budur
sayi = 2

while sayi <= 10:
    sayi += 1
    print(sayi)




