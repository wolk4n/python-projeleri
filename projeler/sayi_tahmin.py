import random

print  ('<<<<<Sayı Tahmin Oyunu>>>>>>  ')
sayi = random.randint(1,100)
tahmin_sayisi = 10

while True:
    kullanici_sayisi = int(input('Sayınız: '))
    if kullanici_sayisi == sayi:
        print('Tebrikler! Doğru Bildiniz.')

    elif kullanici_sayisi > sayi:
        tahmin_sayisi -= 1
        print('Yanlış Tahmin! Lütfen Daha Küçük Bir Sayı Girin.')
        print('Kalan Tahmininiz: ',tahmin_sayisi)

    else:
        tahmin_sayisi -= 1
        print('Yanlış Tahmin! Lütfen Daha Büyük Bir Sayi Girin.')
        print('Kalan Tahmininiz: ',tahmin_sayisi)

    if tahmin_sayisi == 0:
        print('Tahmin Hakkınız Bitti!!!')
        print('Bilgisayarın Tahmin Ettiği Sayı:',sayi)