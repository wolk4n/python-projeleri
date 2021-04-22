kutuphane = ['Python','C++','Ruby'] #* Kütüphanemiz için bir kitap listesi oluşturuyoruz.
secenekler= """

[1] Kitapları Listele
[2] Kitap Ekle
[3] Kitap Sil
[4] Kitap Ara
[5] Çıkış
"""
#? Ana menümüzü yaptık ve secenekler değişkenine atadık

while True: #! PROGRAMIN HEMEN KAPANMAMASI İÇİN WHİLE DÖNGÜSÜNÜ DOĞRU YAPTIK.
    print(secenekler)
    islem = input("İşleminiz: ")
################################ [Kitapları Listele] #########################################
    if islem == "1":
        for sayi,kitap in enumerate(kutuphane):
            print(sayi+1,kitap)
        input("Devam etmek için 'enter'e basın: ")
#*############################## [Kitap Ekle] ################################################# 
    elif islem == "2":
        k_adi = input("Kitap Adı: ")
        kutuphane += [k_adi]
        print("Kitap Eklendi...")
        input("Devam etmek için 'enter'e basın: ")
#?############################## [Kitap Sil] ##################################################
    elif islem == "3":
        durum = False
        k_adi = input("Kitap Adı: ")
        for kitap in kutuphane:
            if k_adi == kitap:
                durum = True
                break
        if durum == True:
            oge_numarasi = kutuphane.index(k_adi)
            del kutuphane[oge_numarasi]
            print("Kitap Silindi...")
        else:
            print("Kitap Mevcut Değil!")
            input("Devam etmek için 'enter' e basın: ")
#*TODO########################## [Kitap Ara] ###################################################
    elif islem == "4":
        k_adi = input("Kitap Adı: ")
        for kitap in kutuphane:
            if kitap == k_adi:
                durum = True
                break
        if durum:
            print("Kitap Kütüphanede Mevcut!")
        else:
            print("Kitap Mevcut Değil!")
#!############################## [Çıkış] #######################################################
    elif islem == "Q" or islem == "q":
        break
    else:
        print("Hatalı Giriş Yapıldı!!!")