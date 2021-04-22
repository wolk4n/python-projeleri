girilen_yazi = input("cümle girin: ") #? Kullanıcıdan bir cümle istiyoruz...
yazinin_tersi = "" #? Boş bir değişken oluşturuyoruz...

#! GİRİLEN CÜMLENİN TERSİNİ ALMAK İÇİN BİR FONKSİYON OLUŞTURUYORUZ.
def tersini_alma(yazi, tersi):
    for i in range(len(yazi) - 1, -1, -1):
        tersi += yazi[i]
    return tersi

#! GİRİLEN CÜMLENİN KELİME KELİME TERSİNİ ALMAK İÇİN BOŞ BİR LİSTE OLUŞTURUYORUZ VE FOR İLE İŞLEMLER YAPIYORUZ...
kelimeler = []
for i in girilen_yazi.split(' '):
    kelimeler.append(tersini_alma(i, ""))

#! KELİME KELİME TERSİNİ ALDIKTAN SONRA BU DEĞERLERİ BİR DEĞERE ATIYORUZ. DAHA RAHAT KULLANMAK İÇİN.
cumle_halinde_tersi = tersini_alma(girilen_yazi, yazinin_tersi)
kelime_halinde_tersi = " ".join(kelimeler)

#! SON OLARAK SONUÇLARI KULLANICIYA SONUÇLARI GÖSTERİYORUZ...
print(
    """
    Cümlenin orjinali:                  {}
    
    Tamamen tersi alınmış hali:         {}
    
    Kelime kelime tersi alınmış hali:   {}
    
    """.format(girilen_yazi, cumle_halinde_tersi, kelime_halinde_tersi))