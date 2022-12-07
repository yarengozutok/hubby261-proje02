import os #standart bir kütüphane modülü içindeki fonksiyon ve nitelikleri kullanabiliriz import ile başka yerden içe aktarıyorum
import time
import urllib.request
from bs4 import BeautifulSoup #from import ile istediğim paketi dahil ediyorum
class GetURL:


    dataFile = "dataURL.txt"
    getFile = "getURL.txt"

    def __init__(self):
        fileTest = open(self.getFile, "a")
        fileTest.close()

    def getWeb(self):

        print("Örümcek çalışıyor...")

        dataOpen = open(self.dataFile, "r")
        getOpen = open(self.getFile, "w")

        for dataGet in dataOpen:
            webSite = urllib.request.urlopen(dataGet)
            getBytes = webSite.read()
            webPage = getBytes.decode("utf8")
            webSite.close()
            soup = BeautifulSoup(webPage, 'html.parser')
            getOpen.write(dataGet.strip() + " - " + soup.title.contents[0] + "\n")
            print(dataGet)
        dataOpen.close()
        getOpen.close()

        print("Çalışma tamamlandı!")

    def getList(self):
        getOpen = open(self. getFile, "r")
        if os.stat(self.getFile).st_size == 0:
            print("Üzgünüm, henüz ziyaret edilmiş adres yok.")
        else:
            print("Ziyaret edilmiş adresler var...")
            print("Lütfen bekleyiniz!")
            time.sleep(1)
        for dataShow in getOpen:
            print(dataShow)
        getOpen.close()
