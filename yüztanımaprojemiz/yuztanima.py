import sqlite3
import tkinter
from tkinter import *
import cv2
import pandas as pd
import xlwt
from datetime import datetime
from datetime import date

ana_pencere = Tk()
ana_pencere.geometry("400x300")
yazi_tipi = "Helvetica 18 bold"
datasets = "yuzler"


def login(): # Giriş fonksiyonu

    k_adi = kullanici_adi.get() # Formdaki bilgileri getir
    parola= sifre.get()

    if k_adi == '' or parola == '':
        mesaj.set("Lütfen tüm alanları doldurun")
    else:
        # veritabanı aç
        conn = sqlite3.connect("personeller.db")
        # sorguyu çalıştır
        cursor = conn.execute('SELECT * from personeller where ADI="%s" and PAROLA="%s"' % (k_adi, parola))
        # veritabınından getirme
        if cursor.fetchone():
            ana_pencere = tkinter.Toplevel()
            # ana_pencere.configure(background='lightgreen')  # Arayüze renk ekleme

            ana_pencere.geometry("400x300")
            yazi_tipi = "Helvetica 18 bold"

            # buton resimleri ekleniyor.
            yoklama = PhotoImage(file=r"kontrol.png")
            yoklamaResim = yoklama.subsample(4, 3)

            baslik = Label(ana_pencere, font=yazi_tipi)
            baslik.grid(column=1, row=2)

            # yoklama alma
            def YoklamaAlma():
                style_string = "font: bold on; borders: bottom dashed"
                style = xlwt.easyxf(style_string)
                style1 = xlwt.easyxf(num_format_str='D-MMM-YY')

                wb = xlwt.Workbook(encoding="utf-8")
                ws = wb.add_sheet('Gelenler', cell_overwrite_ok=True)
                bir_col = ws.col(0)
                bir_col.width = 256 * 20
                iki_col = ws.col(1)
                iki_col.width = 256 * 20
                uc_col = ws.col(2)
                uc_col.width = 256 * 20
                tarih_col = ws.col(4)
                tarih_col.width = 256 * 13

                df = pd.read_excel('personel_listesi.xlsx')
                ad = df['Adı']
                soyad = df['Soyad']
                no = df['Numara']
                uzunluk = len(df)

                ws.write(0, 3, datetime.now(), style1)
                ws.write(0, 0, 'Numara', style=style)
                ws.write(0, 1, 'Adı', style=style)
                ws.write(0, 2, 'Soyad', style=style)
                for z in range(0, uzunluk):
                    ws.write(z + 1, 0, str(no[z]))
                    ws.write(z + 1, 1, ad[z])
                    ws.write(z + 1, 2, soyad[z])
                    ws.write(z + 1, 3, "YOK")

                taniyici = cv2.face.LBPHFaceRecognizer_create()
                taniyici.read('egitim/egitim.yml')
                cascadePath = "haarcascade_frontalface_default.xml"
                faceCascade = cv2.CascadeClassifier(cascadePath);

                cam = cv2.VideoCapture(0,cv2.CAP_DSHOW)
                font = cv2.FONT_HERSHEY_SIMPLEX
                while True:
                    ret, im = cam.read()
                    gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
                    faces = faceCascade.detectMultiScale(gray, 1.2, 5)
                    for (x, y, w, h) in faces:
                        cv2.rectangle(im, (x, y), (x + w, y + h), (150, 0, 0), 2)
                        Id, conf = taniyici.predict(gray[y:y + h, x:x + w])
                        print(conf)
                        b = "TANIMIYOR"
                        for i in range(0, uzunluk):
                            if Id == no[i]:
                                ws.write(i + 1, 3, "VAR", style=style)
                        if conf < 40:
                            cv2.putText(im, str(Id), (x + 5, y + h - 5), font, 0.5, (0, 0, 255), 1, cv2.LINE_AA)
                        else:
                            cv2.putText(im, str(b), (x + 5, y + h - 5), font, 0.5, (0, 0, 255), 1, cv2.LINE_AA)

                    cv2.imshow('YUZ TANIMA UYGULAMASI', im)

                    if (cv2.waitKey(1) == ord('q')):
                        wb.save('Yoklama/gelenler ' + str(date.today()) + '.xls')
                        break
                cam.release()
                cv2.destroyAllWindows()

            yoklamaAl_btn = Button(ana_pencere, text="Yoklama Al", font=yazi_tipi, image=yoklamaResim, compound=TOP,
                                   bg="light green", fg="green", command=YoklamaAlma)
            yoklamaAl_btn.grid(column=0, row=5)

            mainloop()

        else:
            mesaj.set("KULLANICI ADI VEYA ŞİFRE HATALI!!!")


ana_pencere.title("GİRİŞ")

ana_pencere.geometry("550x250")
ana_pencere["bg"] = "#1C2833"

global mesaj
global kullanici_adi
global sifre
kullanici_adi = StringVar()
sifre = StringVar()
mesaj = StringVar()

Label(ana_pencere, width="300", text="GİRİŞ FORMU", bg="#0E6655", fg="white", font=("Arial", 12, "bold")).pack()

Label(ana_pencere, text="Kullanıcı Adı ", bg="#1C2833", fg="white", font=("Arial", 12, "bold")).place(x=20, y=40)

Entry(ana_pencere, textvariable=kullanici_adi, bg="#1C2833", fg="white", font=("Arial", 12, "bold")).place(x=120, y=42)

Label(ana_pencere, text="Şifre ", bg="#1C2833", fg="white", font=("Arial", 12, "bold")).place(x=20, y=80)

Entry(ana_pencere, textvariable=sifre, show="*", bg="#1C2833", fg="white", font=("Arial", 12, "bold")).place(x=120,
                                                                                                                y=82)

Label(ana_pencere, text="", textvariable=mesaj, bg="#1C2833", fg="white", font=("Arial", 12, "bold")).place(x=110,
                                                                                                              y=170)

Button(ana_pencere, text="GİRİŞ", width=10, height=1, command=login, bg="#0E6655", fg="white",
       font=("Arial", 12, "bold")).place(x=115, y=130)
Button(ana_pencere, text="ÇIKIŞ", width=10, height=1, command=ana_pencere.quit, bg="#0E6655", fg="white",
       font=("Arial", 12, "bold")).place(x=230, y=130)

ana_pencere.mainloop()

