import time
from dataURL import DataURL
from getURL import GetURL

useDataURL = DataURL()
useGetURL = GetURL()

print("-:Merhabalar mini örümceğe hoş geldiniz! :-")
print("|-----------------------------------------|")
isim = input("Lütfen isminizi giriniz: ")
print("Merhaba!" '\n' + isim + '\n' "Ben mini örümcek sana nasıl yardımcı olabilirim?" + "\n")
print(" ")
time.sleep(2)

while True:
    print("Lütfen menü numarasını rakam şeklinde giriniz!")
    print("MENÜ: '\n' 0)Çıkış '\n' 1)URL listele '\n' 2)URL ekle '\n' 3)Örümcek gönder '\n' 4)Sonuçları listele '\n'")
    print("Lütfen menü numarasını rakam şeklinde giriniz!")
    menuSecim = (input("Seçiminiz: "))
    if menuSecim.isdigit():
        menuSecim = int(menuSecim)
        if menuSecim == 0:
            print("Mini örümcek kapatılıyor...")
            time.sleep(1)
            break
        elif menuSecim == 1:
            useDataURL.dataRead()
        elif menuSecim == 2:
            useDataURL.dataWrite()
        elif menuSecim == 3:
            useGetURL.getWeb()
        elif menuSecim == 4:
            useGetURL.getList()

    else:
        print("Lütfen menü numarasını 0 ile 4 arasında rakam şeklinde giriniz!")
        print("Yeniden menüye yönlendiriliyorsunuz.Lütfen bekleyiniz...")
        time.sleep(2)