import cv2
import numpy as np
import time
from collections import deque

def main():
    
    yüzdizisi = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    cap = cv2.VideoCapture(0)
    noktalar = deque(maxlen=60)
    zaman = None
    tespitsuresi = 0
    print("Sistem Başlatıldı. Çıkmak için 'q' tuşuna basınız.")

    while True:
        
        ret, cerceve = cap.read()
        if not ret:
            print("Kameradan görüntü alınamadı.")
            break

        cerceve = cv2.flip(cerceve, 1)   
        gri = cv2.cvtColor(cerceve, cv2.COLOR_BGR2GRAY)        
        yüzler = yüzdizisi.detectMultiScale(gri, 1.1, 5)
        if len(yüzler) > 0:
            
            anayüz = max(yüzler, key=lambda rect: rect[2] * rect[3])
            (x, y, w, h) = anayüz
            cv2.rectangle(cerceve, (x, y), (x + w, y + h), (0, 255, 0), 2)
            merkez_x = int(x + w / 2)
            merkez_y = int(y + h / 2)
            merkez_nokta = (merkez_x, merkez_y)
            noktalar.appendleft(merkez_nokta)
            coord_text = f"Merkez Koordinat: X: {merkez_x}, Y: {merkez_y}"
            cv2.putText(cerceve, coord_text, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 
                        0.7, (255, 0, 0), 2)
            
            if zaman is None:
                zaman = time.time() 
            şimdiki_zaman = time.time()
            tespitsuresi = şimdiki_zaman - zaman
            zamanlayıcı = f"Sure: {tespitsuresi:.2f} sn"
            cv2.putText(cerceve, zamanlayıcı, (cerceve.shape[1] - 250, 30), 
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

        else:
            zaman = None
            tespitsuresi = 0
        for i in range(1, len(noktalar)):
            if noktalar[i - 1] is None or noktalar[i] is None:
                continue
            kalınlık = 2
            cv2.line(cerceve, noktalar[i - 1], noktalar[i], (0, 0, 255), kalınlık)

        cv2.imshow('Ödev 4: Yüz Takip', cerceve)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
