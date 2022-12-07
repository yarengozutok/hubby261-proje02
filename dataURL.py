import os
import time


class DataURL:
    dataFile = "dataURL.txt"

    def __init__(self):
        fileTest = open(self.dataFile, "a")
        fileTest.close()

    def dataWrite(self):
        dataOpen = open(self.dataFile, "a")
        siteURL = input("Lütfen site adresini ön eki ile birlikte giriniz: ")
        kontrolHTTP = siteURL[:7]
        kontrolHTTPS = siteURL[:8]
        if kontrolHTTP == "http://" or kontrolHTTPS == "https://":
            print("Adres girişi doğru.")
            print("Lütfen bekleyiniz!")
            time.sleep(2)
            print("Adres listeye eklendi. Teşekkürler!")
        else:
            print("Hatalı adres girişi yaptınız!")
            time.sleep(1)
            print("Lütfen site adresini ön eki ile birlikte 'http veya https' şeklinde giriniz.")
            print("Ana menüye yönlendiriliyorsunuz...")
            time.sleep(2)

        dataOpen.write(siteURL + "\n")
        dataOpen.close()

    def dataRead(self):
        dataOpen = open(self.dataFile, "r")
        if os.stat(self.dataFile).st_size == 0:
            print("Üzgünüm...henüz kaydedilmiş adres yok!")
        else:
           print("Kaydedilmiş adresler var...")
           print("Kaydedilmiş adresleri listeliyorum!")
           time.sleep(1)
        for dataShow in dataOpen:
            print(dataShow)
        dataOpen.close()
