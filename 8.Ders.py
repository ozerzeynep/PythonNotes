#BREAK
#İçinde bulunduğu döngüyü kırar, bitirir.

harfler = ['a','b','c','d','e']

for index,harf in enumerate(harfler):
    if harf == 'c':
        print("{} harfi {}. indexte yer alır".format(harf,index))
        break


maaslar = [80000,70000,5000,1000,30000,400000,2000]
maaslar.sort()
for i in maaslar:
    if i == 30000:
        print("Döngü sonlandırıldı.")
        break
    print(i)


#CONTINUE
#Sadece o tur için döngüyü kırar. Yoksayma işlemini yapar. Koşulları teker teker kontrol eder. Break gibi yanlış konşulu gördüğünde direk döngüyü sonlandırma işlemini yapmaz. Aynı yorum satırını derleyicinin görmeyip yok sayıp alttaki kod ifadesinden devam etmesi gibi düşüne bilirsiniz.
    

maaslar = [80000,70000,5000,1000,30000,400000,2000]
maaslar.sort()
for i in maaslar:
    if i == 30000:
        print("Döngü sonlandırıldı.")
        continue
    print(i)


#Tek olan sayıları bulma
for sayi in range(1,36):
    if sayi %2 == 0:
        continue
    print(sayi)


