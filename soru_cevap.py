print("soru-cevap programına hoş geldiniz") #* Kullanıcımızı hoşgeldin mesajı ile karşılıyoruz.
ad = str(input("adınızı girin: ")) #* Kulllanıcının adını istiyoruz.
print("hadi başlayalım",ad,"!!!") #* Kullanıcıya programın başladığı ile ilgili mesaj veriyoruzç

#! İLK SORUMUZU SORUYORUZ. DİĞER SORULAR DA BU MANTIK İLE YAZILMIŞTIR.
soru1 = input("""
============================================
Soru 1-) Osmanlı Devletini Kim Kurmuştur?
A) orhan bey
B) yıldırım beyazıt
C) osman bey
D) 1.mehmet (çelebi mehmet)
============================================
Cevabınızı giriniz: """) #? İlk önce sorumuzu print() komutu ile sorduk ve soru1 değişkenine atadık.

if soru1 == "C" or soru1 == "c": #? Eğer kullanıcı soruya "C" veya "c" cevabı verirse "doğru cevap" yazıyoruz.
    print("doğru cevap")

elif soru1 == "A" or soru1 == "a": #? Eğer kullanıcı soruya "A" veya "a" cevabı verirse "yanlış cevap", "doğru cevap C" yazıyoruz.
    print("yanlış cevap\ndoğru cevap C")

elif soru1 == "B" or soru1 == "b":
    print("yanlış cevap\ndoğru cevap C") #? Eğer kullanıcı soruya "B" veya "b" cevabı verirse "yanlış cevap", "doğru cevap C" yazıyoruz.

elif soru1 == "D" or soru1 == "d":
    print("yanlış cevap\ndoğru cevap C") #? Eğer kullanıcı soruya "D" veya "d" cevabı verirse "yanlış cevap", "doğru cevap C" yazıyoruz.

else: #! Eğer soruya a,b,c veya d dışında farklı bir cevap verirse kullanıcıya hata mesajı veriyoruz.
    print("yanlış karakterler girdiniz a,b,c veya d girmeliydiniz")

soru2 = input("""
====================================================================================
Soru 2-) Osmanlı Devletinde İlk Gümüş Para Hangi Padişah Tarafından Kullanılmıştır?
A) osman bey
B) orhan bey
C) fatih sultan mehmet
D) yıldırım beyazıt
====================================================================================
cevabınızı giriniz: """)

if soru2 == "B" or soru2 == "b":
    print("doğru cevap")

elif soru2 == "A" or soru2 == "a":
    print("yanlış cevap\ndoğru cevap B")

elif soru2 == "C" or soru2 == "c":
    print("yanlış cevap\ndoğru cevap B")

elif soru2 == "D" or soru2 == "d":
    print("yanlış cevap\ndoğru cevap B")


else:
    print("yanlış karakterler girdiniz a,b,c veya d girmeliydiniz")


soru3 = input("""
====================================================================
Soru 3-) "6 . ( x + 4 ) + 3 . ( x - 8 ) = 45" Olduğuna Göre, x Kaçtır ?
A) 4
B) 5
C) 6
D) 7
====================================================================
cevabınızı giriniz: """)

if soru3 == "B" or soru3 == "b":
    print("doğru cevap")

elif soru3 == "A" or soru3 == "a":
    print("yanlış cevap\ndoğru cevap B")

elif soru3 == "C" or soru3 == "c":
    print("yanlış cevap\ndoğru cevap B")

elif soru3 == "D" or soru3 == "d":
    print("yanlış cevap\ndoğru cevap B")

else:
    print("yanlış karakterler girdiniz a,b,c veya d girmeliydiniz")

soru4 = input("""
====================================================================
Soru 4-) Nene Hatununda Savaştığı Osmanlı-Rus Savaşının Adı Nedir?
A) çanakkale savaşı
B) 1.dünya savaşı
C) 93 harbi
D) kurtuluş savaşı
====================================================================
cevabınızı girin: """)

if soru4 == "C" or soru4 == "c":
    print("doğru cevap")

elif soru4 == "A" or soru4 == "a":
    print("yanlış cevap\ndoğru cevap C")

elif soru4 == "B" or soru4 == "b":
    print("yanlış cevap\ndoğru cevap C")

elif soru4 == "D" or soru4 == "d":
    print("yanlış cevap\ndoğru cevap C")

else:
    print("yanlış karakterler girdiniz a,b,c veya d girmeliydiniz")

soru5 = input("""
====================================================================
Soru 6-) Türkün Siber Ordusu Ayyıldız Tim Kaç Yılında Kurumuştur ?
A) 1990
B) 2002
C) 1999
D) 2006
====================================================================
cevabınızı girin: """)

if soru5 == "D" or soru5 == "d":
    print("yanlış cevap\ndoğru cevap B")

elif soru5 == "A" or soru5 == "a":
    print("yanlış cevap\ndoğru cevap B")

elif soru5 == "B" or soru5 == "b":
    print("doğru cevap")

elif soru5 == "C" or soru5 == "c":
    print("yanlış cevap\ndoğru cevap B")

else:
    print("yanlış karakterler girdiniz a,b,c veya d girmeliydiniz")

cik = input("oyun bitti. Çıkmak için q tuşuna basın: ")
print("hoşcakal", ad , ":)")

if cik == "q" or cik == "Q":
    print("çıkılıyor...")
    exit()

else:
    print("q tuşuna basın dedim ama olsun.")
    time.sleep(3)
    exit()