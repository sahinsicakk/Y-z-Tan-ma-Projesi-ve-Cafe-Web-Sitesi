import cv2
import numpy as np
from PIL import Image
import os


path = 'datasets' # Verilerin yolu
#recognizer = cv2.face.LBPHFaceRecognizer_create()
taniyici = cv2.face.LBPHFaceRecognizer_create()
detector = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

# imajların alınması ve etiketlenmesi için fonksiyon
def getImagesAndLabels (path):
    resim_yolu= [os.path.join(path,f) for f in os.listdir(path)]
    ornekler=[]
    ids = []
    for res_yol in resim_yolu:
        resmi_isle= Image.open(res_yol).convert('L')    # gri
        dizi_yap = np.array(resmi_isle,'uint8')
        id = int(os.path.split(res_yol)[-1].split(".")[0])
        print("id= ",id)
        yuzler = detector.detectMultiScale(dizi_yap)
        for (x,y,w,h) in yuzler:
            ornekler.append(dizi_yap[y:y+h,x:x+w])
            ids.append(id)
    return ornekler,ids
print ("\n [INFO] yuzler eğitiliyor. Bekleyin lütfen ...")
yuzler,ids = getImagesAndLabels(path)
taniyici .train(yuzler, np.array(ids))
# Modeli egitim/egitim.yml dosyasına kaydet
taniyici.write('egitim/egitim.yml') # Dikkat! recognizer.save() Raspberry Pi üzerinde çalışmıyor
# Eğitilen yüz sayısını göster ve kodu sonlandır
print(f"\n [INFO] {len(np.unique(ids))} yüz eğitildi. Betik sonlandırılıyor.")

# print(yuzler)