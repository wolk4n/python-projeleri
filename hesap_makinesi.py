sayi1 = int(input("1. Sayıyı Giriniz: ")) #* Kullanıcıdan int yani sayısal bir değer istiyoruz.
sayi2 = int(input("2. Sayıyı Giriniz: ")) #* Kullanıcıdan ikinci bir int değeri istiyoruz.

secim = input(("Yapıcağınız İşlem +,-,/,* : ")) #* Kullanıcıdan işlem yapmak için değer istiyoruz. (+,-,/,*) gibi.

if (secim=="+"): #! Eğer kullanıcı yukarıda vermiş olduğumuz işleme "+" girer ise:
    islem = sayi1 + sayi2 #? sayi1 ve sayi2' yi toplayıp sonucu "islem" değişkenine atar. 
    print("İşleminizin sonucu:",islem) #? Ve son olarak islemin sonucunu ekrana yazdırıyoruz. 

#*TODO: Ve aşağıdaki diğer işlemler için de aynı mantığı kullanırız. 

elif (secim=="-"):
    islem = sayi1 - sayi2
    print("İşleminizin sonucu:",islem)

elif (secim=="/"): 
    islem = sayi1 / sayi2
    print("İşleminizin sonucu:",islem)

elif (secim=="*"):
    islem = sayi1 * sayi2
    print("İşleminizin sonucu:",islem)

else:
    print("Hatalı veya Eksik Tuşladınız...")