import tkinter as tk
from tkinter import *
import time
from dataURL import DataURL
from getURL import GetURL

pencere = tk.Tk()
pencere.title("Ana Pencere")
pencere.geometry("300x200")

def pencereA():
    pencere2 = Tk()
    pencere2.title("PencereA")
    pencere2.geometry("300x200")
    buton2 = Button(pencere2, text= "Kapat", command=pencere2.destroy)
    buton2.pack()

def pencereB():
    pencere3 = Tk()
    pencere3.title("PencereB")
    pencere3.geometry("300x200")
    buton3 = Button(pencere3, text="Kapat", command=pencere3.destroy)
    buton3.pack()

def pencereC():
    pencere4 = Tk()
    pencere4.title("PencereC")
    pencere4.geometry("300x200")
    buton4 = Button(pencere4, text="Kapat", command=pencere4.destroy)
    buton4.pack()

def pencereD():
    pencere5 = Tk()
    pencere5.title("PencereD")
    pencere5.geometry("300x200")
    buton5 = Button(pencere5, text="Kapat", command=pencere5.destroy)
    buton5.pack()

def pencereE():
    pencere6 = Tk()
    pencere6.title("PencereE")
    pencere6.geometry("300x200")
    buton6 = Button(pencere6, text="Kapat", command=pencere6.destroy)
    buton6.pack()

etiket = Label(pencere, text="Merhaba ben mini örümcek!")
etiket2 = Label(pencere, text="Size nasıl yardımcı olabilirim?")

etiket3 = Label(pencere, text="Menü")

etiket.pack()
etiket2.pack()
etiket3.pack()

butonA = Button(pencere, text= "0) Çıkış ", command=pencereA)
butonA.pack()

butonB = Button(pencere, text= "1) URL Lİstele", command=pencereB)
butonB.pack()

butonC = Button(pencere, text= "2) URL Ekle", command=pencereC)
butonC.pack()

butonD = Button(pencere, text= "3) Örümcek Gönder", command=pencereD)
butonD.pack()

butonE = Button(pencere, text= "4) Sonuçları Listele", command=pencereE)
butonE.pack()

pencere.mainloop()

useDataURL = DataURL()
useGetURL = GetURL()

while True:
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