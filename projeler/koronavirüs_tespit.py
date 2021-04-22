print('KORONA VİRÜS TESPİT PROGRAMINA HOŞGELDİNİZ ÖNCELİKLE;\nEğer semptomları gösteriyorsanız evde izole şekilde geçmesini bekleyiniz.\nFakat kötü durumda iseniz yakınınızda bulunana en yakın sağlık kuruluşuna başvurunuz...')
#! İLK ÖNCE KULLANICIYA BELİRTİLEN SEMPTOMLARI GÖSTERDİĞİ TAKDİRDE NE YAPMASI GEREKTİĞİNİ YAZIYORUZ!
isim = input('isim: ') #? Burada kullanıcının ismini alıyoruz.

#*TODO: Burada ise semptomlardan hangilerini gösterdiğini anlamak için sorular soruyoruz...
print('\nBu semptomlardan hangilerini kendinde gözlemliyorsun?')
ates = int(input('Ateşin var mı? (0= yok, 1= var): '))
oksur = int(input('Öksürük var mı? (0= yok, 1= var): '))
nd = int(input('Nefes darlığı var mı? (0= yok, 1= var): '))
bog = int(input('Boğaz ağrısı veya burun akıntısı var mı? (0= yok, 1= var): '))
kus = int(input('Kusma durumu var mı? (0= yok, 1= var): '))
hastalik = int(input('Diyabet, böbrek veya kalp hastalığı var mı? (0= yok, 1= var): '))
bolge = int(input('Son 14 günde salgın bölgesinde veya bu bölgeden biriyle temas halinde bulundun mu?(0= hayır, 1= evet): '))
#*TODO##########################################################################################################################

tehlike = ates*2 + oksur*2 + nd*2 + bog + kus + hastalik #? Kullanıcının vermiş olduğu cevaplar ile bir tehlike seviye oluşturuyoruz.

#! BURADA İSE KULLANICIYA ÇIKAN SONUÇLARI GÖSTERİYORUZ...
print(isim+',')
if bolge ==0:
    if tehlike > 4: print("Belirttiğin semptomlar COVID-19 için ciddi risk teşkil etmiyor,muhtemelen gripsin.")
    else: print("Enfekte olma ihtimalin var,kendine dikkat et dostum.")
if bolge ==1:
    if tehlike > 4: print('Enfekte olma ihtimalin hayli yüksek,teyit edilene kadar maske kullanıp ve kendine dikkat etmelisin.')
    else: print("Enfeksiyon belirtileri düşük,ama yine de bölgeden dolayı enfekte olma tehliken var. ")
print("Sağlıklı Günler Dileriz...")

