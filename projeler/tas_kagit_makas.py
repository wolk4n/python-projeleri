import random #! Rnadom modülünü programımıza ekliyoruz bu modül programın rastgele bir değer almasını sağlayacaktır.

#*TODO: Programın rastgele seçimler yapması için değişkenleri oluşturuyoruz...
secenek=["taş","kağıt","makas"] 
taş=secenek[0]
kağıt=secenek[1]
makas=secenek[2]

print("Taş,Kağıt, Makas oyununa hoş geldiniz") #? Oyunumuzun ana menüsü.

secim = input("Taş mı kağıt mı makas mı? ") #Kullanıcıdan Taş, Kağıt veya Makas değerini istiyoruz.
bil_secim = random.choice(secenek) #* Program yukarıda belirtmeiş olduğumuz secenek listesinden rastgele bir değer alıyor.
#! BURADAN SONRASI BASİT İF ELSE MANTIĞIDIR.
if secim==taş:
    if bil_secim==taş:
        print("Bilgisayarın seçimi: Taş\nSonuç: Berabere")
    elif bil_secim==kağıt:
        print("Bilgisayarın seçimi: Kağıt\nSonuç: Kaybettiniz")
    else:
        print("Bilgisayarın seçimi: makas\nSonuç:Kazandınız")
if secim==kağıt:
    if bil_secim==taş:
        print("Bilgisayarın seçimi: Taş\nSonuç: Kazandınız")
    elif bil_secim==kağıt:
        print("Bilgisayarın seçimi: Kağıt\nSonuç: Berabere")
    else:
        print("Bilgisayarın seçimi: makas\nSonuç:Kaybettiniz")
if secim==makas:
    if bil_secim==taş:
        print("Bilgisayarın seçimi: Taş\nSonuç: Kaybettiniz")
    elif bil_secim==kağıt:
        print("Bilgisayarın seçimi: Kağıt\nSonuç: Kazandınız")
    else:
        print("Bilgisayarın seçimi: makas\nSonuç:Berabere")