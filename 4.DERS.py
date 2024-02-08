#İF SORGUSU
#KULLANIM ŞEKLİ => İF(KOŞUL SAĞLANIYORSA):
                        #(BURADA YAZILANI YAP)

hava_durumu = "yağışlı"
if hava_durumu == "yağışlı":
    print("Şemsiyeni Al")
else:
    print("Önemli Değil")


print("*****************************************")

basarı_durumu = "İyi"
if basarı_durumu == "İyi":
    print("Öğrenci Başarılıdır")
else:
    print("Öğrenci Başarısızdır!!!!!!")

basarı_durumu1 = "İyi"
if basarı_durumu1 == "Kötü":
    print("Öğrenci Başarılıdır")
else:
    print("Öğrenci Başarısızdır!!!!!!")
    

print("//////////////////////////////////////////////////////////////")

donem_dersi = "Veri Tabanı Yönetim Sistemleri"
if donem_dersi == "Python":
    print("Dönem Dersi Ekranda Belirtildi")
elif donem_dersi == "Veri Tabanı Yönetim Sistemleri":
    print("Doğru Olan Dönem Dersi Ekranda Belirtildi")
else:
    print("Dönem Dersi Ekranda Belirtilmemiştir")

hava = "güneşli"
if hava == "yağışlı":
    print("Şemsiyeni Al")
else:
    print("Sorun Değil")
    
hava1 = "güneşli"
if hava1 == "yağışlı":
    print("Şemsiyeni Al")
elif hava1 == "güneşli":
    print("Güneş Parıl Parıl ve Güneş Kremini Sür")
else:
    print("Hava Kapalı Sanırım")
    

print("------------------------------------------------------------------------------")

ders = ["Veri Tabanı Yönetim Sistemleri", "Yapay Zeka", "Üretim Yönetim Sistemleri"]
hedef_ders = "Görsel Programlama"
if hedef_ders in ders:
    print("Dönem Dersiniz İçinde Bulunmaktadır")
else:
    ders.append(hedef_ders)
    print("İstenilen Ders Sisteminiztde Yoktu Ama Şimdi Eklendi")
    print("Derslerinizin Son Hali {}".format(ders))
   
    

print("------------------------------------------------------------------------------")



yas = 35
if yas > 18:
    print("İçeri Girebilirsiniz")
else:
    print("İçeri Giremezsiniz")

yası = 22
if yası < 18:
    print("İstediğinizi Alabilir Siniz")
elif yası <= 20:
    print("Ailenizle Beraber İstediğinizi Alabilirsiniz")
else:
    print("İstediğinizi Alamazsınız")


liste = ['a','b','c']
hedef_harf = 'd'
if hedef_harf in liste:
    print("Liste İçinde Bulunur")
else:
    print("Liste İçinde Yoktur")


liste1 = ['a','b','c']
harf = 'd'
if harf in liste:
    print("Liste İçinde Bulunur")
else:
    liste1.append(harf)
    print("İstediğiniz Harf Eklendi")
    print("Güncel Liste {}".format(liste1))

liste2 = ['a','b','c','d']
harf = 'd'
if (harf in liste2) and (harf == liste2[0]):
    print("Buldum ve İlk Harf Konumunda")
elif harf in liste2:
    print("Buldum ama İlk Harf Konumunda Değil")
else:
    print("Bulamadım")
    


x = 10
y = 5
if x > 8 and y > 3:
    print("İstediğim Değer Aralığında")
else:
    print("İstediğim Değer Aralığında Değil")
    


family = ["Zeynep Özer", "Reyhan Özer", "İlknur Özer", "Hakan Özer"]
uye = ["Muteber Pak"]
if uye in family:
    print("Üye bu aileye ait.")
else:
    print("Üye bu aileye ait değil.")


sınıf = ["Aylin Çalış", "Neriman Göksel", "Ozan Kaya", "Utku Ateş", "Poyraz Şimşek", "Kuzey Atalar", "Mina Gül"]
uyeler = ["Ayla Öztürk"]
if uyeler in sınıf:
    print("Sınıf öğrencisi burada, bulduk")
else:
    sınıf.append(uyeler)
    print("Üye burada değildi ama eklendi")
    print("Sınıf listesinin Güncel Hali {} budur".format(sınıf))
    

ortalaması = 70
istenen_net = 85
if ortalaması == istenen_net:
    print("Öğrenci Başarılıdır")
    print("Öğrcencinin Notu {} budur".format(ortalaması))
elif ortalaması != istenen_net:
    print("Öğrenci Orta Düzeydedir")
    print("Öğrcencinin Notu {} budur".format(ortalaması))
else:
    print("Öğrenci Başarılı Değildir")


sınıf_ortalaması = 55
istenen_sınıf_ortalaması = 80
if (sınıf_ortalaması == istenen_sınıf_ortalaması) and (sınıf_ortalaması>50):
    print("Sınıfın Durumu Gayet İyidir")
    print("Güncel Ortalamaları İse {}".format(sınıf_ortalaması))
elif (sınıf_ortalaması < istenen_sınıf_ortalaması) and (sınıf_ortalaması >= 50):
    print("Sınıfın Durumu Yeteri Kadar Da İyi Değildir")
    print("Güncel Ortalamaları İse {}".format(sınıf_ortalaması))
else:
    print("Sınıf Çok Kötü Durumdadır")




elemanlar = ["Ali Söylemez", "Ahsen Mutlu", "Kamil Kara", "Poyraz Arseven", "Kuzey Kayalı", "Pınar Özlü"]
atılacak_eleman = "Kamil Kara"
if atılacak_eleman in elemanlar:
    elemanlar.remove("Kamil Kara")   #remove ile listeden istediğimiz elemanı çıkartabiliriz
    print("Eleman Kayıt Listesinden Çıkartıldı")
    print("Listedeki Elemanların Son Hali {}".format(elemanlar))
else:
    print("İşlem Başarısız Oldu")



sayi1 = 30
sayi2 = 55
if sayi1 == sayi2:
    print("Değerler Birbirlerine Eşit Bulundu")
else:
    sayi1 = sayi1 + sayi2
    print("Sayının Son Hali {}".format(sayi1))



sayi3 = 30
sayi4 = 55
if sayi3 == sayi4:
    print("Değerler Birbirlerine Eşit Bulundu")
elif sayi3 < sayi4:
    sayi3 = sayi3 * sayi4
    print("Sayının Son Değeri {}".format(sayi3))
else:
    sayi3 = sayi3 + sayi4
    print("Sayının Son Hali {}".format(sayi3))
    
    
    










