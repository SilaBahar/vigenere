turkce_alfabe = [                                               # türkçe alfabesinin harflerini içeren liste
        'a', 'b', 'c', 'ç', 'd', 'e', 'f', 'g', 'ğ', 'h',
        'ı', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'ö', 'p',
        'r', 's', 'ş', 't', 'u', 'ü', 'v', 'y', 'z'
    ]

#word = input("bir kelime gir:")

def sayıya_çevirme(kelime,x) :     # kelimenin harflerini sayı değerlerine çeviren fonksiyon
    harfdeğerleri = []         # harflerin sayı değerleri için boş liste açıyor
    for harf in kelime:               # kelimenin içinden teker teker harfleri alır
        sayı_değeri = turkce_alfabe.index(harf) + x    # her bir harfin alfabedeki indexini alır (eğer başta x değerine 1 verdiyse harflerin sıra sayılarına 1 eklenir)
        harfdeğerleri.append(sayı_değeri)      # her harfin alfebedeki sayı değerini listeye ekler
    #print(harfdeğerleri)
    return harfdeğerleri     # listeyi returnlüyor(?)


def toplama(şifresizMetin, anahtar) : # metnin ve anahtarın sayı değerlerini metnin uzunluğuna göre toplar
    toplamlar = []     # toplam için boş liste şysisi açıyor
    anahtar_uzunluğu = len(anahtar) # anahtar lisresinde kaç adet değer olduğunu hesaplar
    for i in range(len(şifresizMetin)):  # şifreli metinin uzunluğu kadar indexleri teker teker alır
        toplam = (şifresizMetin[i]  +  anahtar[i % anahtar_uzunluğu]) % 29 #
        toplamlar.append(toplam) 
    return toplamlar

def çıkarma(şifreliMetin, anahtar):   # metnin ve anahtarın sayı değerlerini metnin uzunluğuna göre farkını hesaplar
    farklar = []            # farkları için boş liste şesisi açıyor
    anahtar_uzunluğu = len(anahtar)     # anahtar listesinde kaç adet değer olduğunu hesaplar
    for i in range(len(şifreliMetin)):     # şifreli metinin uzunluğu kadar indexleri teker teker alır
        fark = (şifreliMetin[i] - anahtar[i % anahtar_uzunluğu]) % 29   # ...
        farklar.append(fark)      # "farklar" listesine tüm harflerin "fark"ları ekler
    return farklar


def harfe_çevir(sayı_listesi,x):
    if (x==0):
        metin = ""
        for sayı in sayı_listesi:
            metin += turkce_alfabe[sayı]
        return metin
    elif (x==1):
        metin = ""
        for sayı in sayı_listesi:
            metin += turkce_alfabe[sayı-1] 
        return metin    

def şifreli_metin_çözme(şifreliMetin, anahtar, x):
    şifreli_kodun_değerleri = sayıya_çevirme(şifreliMetin, x)   # girilen şifreli metni sayı değerlerine çevirip şifreli_kodun_değerleri'ne eşitldi 
    print(şifreli_kodun_değerleri)        # şifreli kodun sayı değerlerini yazdırır

    anahtarın_değerleri = sayıya_çevirme(anahtar, x)  # girilen anahtarı sayı değerlerine çevirip anahtarın_değerler'ne eşitldi
    print(anahtarın_değerleri)         # anahtarın sayı değerlerini yazdırır

    şifresiz_sayılar = çıkarma(şifreli_kodun_değerleri, anahtarın_değerleri)       # şifresiz sayı listesini bulmak için çıkarma fonksiyonutla şifreli kodun sayı değerlerinden anahtarın sayı değerlerini çıkarır 
    print(şifresiz_sayılar)        # şifresiz sayı listesini yazdırır

    şifresiz_metin = harfe_çevir(şifresiz_sayılar, x)       # şifresiz metnin sayı değerlerini harfe çevir fonksiyonuyla metin hale çevirir
    print(şifresiz_metin)       # terminale sonucu yazdırır
    return şifresiz_metin

def şifreli_metine_çevirme(şifresizMetin, anahtar, x):
    şifresiz_kodun_değerleri = sayıya_çevirme(şifresizMetin, x)  
    print(şifresiz_kodun_değerleri)        
    anahtarın_değerleri = sayıya_çevirme(anahtar, x)  
    print(anahtarın_değerleri)        
    şifreli_sayılar = toplama(şifresiz_kodun_değerleri, anahtarın_değerleri)     
    print(şifreli_sayılar)      
    şifreli_metin = harfe_çevir(şifreli_sayılar, x)       
    print(şifreli_metin)      
    return şifreli_metin


while True:
    x = int(input("1e göre mi 0a göre mi:"))

    if (x == 0 or x == 1):
        print("0 yada 1e denk")
        break
    else:
        print("x'e 1 ya da 0 değerini veriniz")
        continue



while True:
    a = int(input("şifreli metninizi çözmemizi istiyorsanız 1, \n şifreli metine çevirmemizi istiyorsanız 0 yazın:"))
    if a==1:
        şifrelimetin = input("şifreli metini girin:") # girilen şifreli metni saklıyor
        key = input("anahtarı girin:") # girilen anahtarı saklar
        şifreli_metin_çözme(şifrelimetin, key, x)
        break
    elif a==0:
        şifresizmetin = input("şifresiz metini girin:") 
        key = input("anahtarı girin:") 
        şifreli_metine_çevirme(şifresizmetin, key, x)
        break
    else:
        print("a'ya 1 ya da 0 değerini veriniz") 
        continue 






        



print 
