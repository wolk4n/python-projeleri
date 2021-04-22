import time #! TİME YANİ ZAMAN MODÜLÜNÜ PROGRAMIMIZA EKLİYORUZ. BU MODÜL PROGRAMIN ZAMAN İŞLERİNİ YAPICAKTIR.

print('Alarm Kurmak istediğiniz Zamanı Giriniz: ') #* Kullanıcıyı karşılıyoruz.
print('-'*40) #* Görsellik açısından 40 kere "-" işareti koyuyoruz.
time.sleep(1) #* ve 1 saniye bekliyoruz.

saat=int(input('Saat : ')) #? Kullanıcıdan saat değeri istiyoruz.
dakika=int(input('Dakika: ')) #? Ve daha sonra dakika değerini istiyoruz.


while True: #! SAAT VE DAKİKA DEĞERLERİNİ GİRDİKTEN SONRA PROGRAMIN KAPANMAMASI İÇİN WHİLE DEĞERİNİ DOĞRU OLARAK AYARLIYORUZ.
    zaman = time.localtime(time.time()) #? zaman değişkenine güncel olarak yerel saat değerini atıyoruz. 
    if (saat == zaman.tm_hour and dakika == zaman.tm_min): #* Bizim girdiğimiz saat ve dakika değeri zaman değişkenine eşit ise: 
        print('Alarm Çalıyor Saat:{}.{}'.format(saat,dakika)) #* "Alarm Çalıyor Saat: xx.xx" şeklinde uyarı veriyoruz.
        break #* Ve programı kapatıyoruz.
    else: #! Eğer böyle olmazsa: 
        continue #? Program kapanmıyor devam ediyor. Saat ve Dakika değerleri yerel saate eşit olana kadar...

