# Mengimport package yg diperlukan
import cv2, time
import os
from PIL import Image
import mediapipe as mp
#import serial
#arduino = serial.Serial(port='COM3', baudrate=9600, timeout=2)

# inisialisasi varibel hand tracking
mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

pTime = 0
cTime = 0

# camera = 0 berarti menggunakan web cam bawaan perangkat. Ubah 0 jika menggunakan webcam external
camera = 0

# Inisialisasi video capture
# cv2 -> modul open-cv
#videoCapture() -> object dari opencv dengan parameter (source, CAP_DSHOW = DirectShow sebagai video input)
video = cv2.VideoCapture(camera, cv2.CAP_DSHOW)

# cascade classifier menggunakan file haarcascade yang ada
# CascadeClassifier(source) -> objet dari opencv yang membaca classifier yang akan digunakan 
faceDeteksi = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# face.LBPHFaceRecognizer_create() -> membuat pengenalan dengan menggunakan algoritma LBPH(Local Binary Pattern)
recognizer = cv2.face.LBPHFaceRecognizer_create()

# recognizer membaca file training.xml
recognizer.read('Dataset/training.xml')

# deklarasi variabel a
a = 0
# Program webcam akan terus berjalan selama bernilai TRUE
while True:
    # Iterasi variabel a (a+1)
    a = a + 1
    # Membuat cam di frame windows
    check, frame = video.read()
    # cvtColor(frame, mode warna) -> object dalam cv2 untuk menentukan mode warna dalam frame
    # COLOR_BGR2GRAY -> mengubah mode warna (Blue Green Red) menjadi Gray
    abu = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    imgRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)

    # implementasi hand tracking

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            for idh, lm in enumerate(handLms.landmark):
                # print(id, lm)
                h, w, c = frame.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                print(idh, cx, cy)
                # if id == 4:
                cv2.circle(frame, (cx, cy), 15, (255, 0, 255), cv2.FILLED)

            mpDraw.draw_landmarks(frame, handLms, mpHands.HAND_CONNECTIONS)

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    cv2.putText(frame, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3,
                (255, 0, 255), 3)

    # detecMultiScale() -> object untuk Mendeteksi wajah, dengan paramter (mode gambar, faktor scala, spesifik berapa Neightboors kandidat)
    wajah = faceDeteksi.detectMultiScale(abu,1.3,5)
    for(x,y,w,h) in wajah :
        # Membuat kotak hijau di wajah
        cv2.rectangle(frame, (x,y),(x+w,y+h),(0,255,0),2)
        id, conf = recognizer.predict(abu[y:y+h, x:x+w])

        # Seleksi Id
        if (id == 1):
            id = 'Aizin'
            senyum = 3 # mood happy
            #arduino.write(f"{senyum}\n".encode())
            #time.sleep(0.1)
        elif (id == 2):
            id = 'Albert'
            senyum = 3 # mood happy
            #arduino.write(f"{senyum}\n".encode())
            #time.sleep(0.1)
        elif (id == 3):
            id = 'Arya'
        elif (id == 4):
            id = 'Roy'
        elif (id == 5):
            id= 'Aldi'
        elif (id == 6):
            id ='Hermawan'
        else:
            id = 'Alien'

        # Menambahkan teks sesuai Id ke wajah didalam frame
        cv2.putText(frame, str(id),(x+40, y-10), cv2.FONT_HERSHEY_DUPLEX,1,(0,255,0))
    # imshow untuk memberikan label pada frame saat window terbuka

    cv2.imshow("Face Recognation", frame)
    # menentukan keyboard event
    key = cv2.waitKey(1)

    # Cam berhenti saat menekan tombol q pada keyboard
    if key == ord('q'):
        break

# Camera berhenti
video.release()
cv2.destroyAllWindows()