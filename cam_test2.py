import cv2
from cv2 import aruco

# Harici kamerayı aç (kamerayı 1 ile başlatıyoruz, yerleşik kamera için 0 olabilir)
cap = cv2.VideoCapture(1)  # Logitech kamerayı kullanmak için 1

# Kameranın açıldığını kontrol et
if not cap.isOpened():
    print("Kamera açılamadı!")
    exit()

# Kameradan bir kare almaya çalış
ret, frame = cap.read()
if not ret:
    print("Kare alınamadı, kamera ile ilgili bir problem olabilir.")
    exit()

# Aruco sözlüğü ve parametreler
aruco_dict = aruco.getPredefinedDictionary(aruco.DICT_4X4_50)
parameters = aruco.DetectorParameters()  # Burada düzeltme yaptık

while True:
    ret, frame = cap.read()

    if not ret:
        print("Kare alınamadı, kamera ile ilgili bir problem olabilir.")
        break

    # Markerları tespit et
    corners, ids, rejectedImgPoints = aruco.detectMarkers(frame, aruco_dict, parameters=parameters)

    # Markerları çiz
    frame_markers = aruco.drawDetectedMarkers(frame, corners, ids)

    # Görüntüyü göster
    cv2.imshow("Aruco Marker Detection", frame_markers)

    # 'q' tuşuna basıldığında çık
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Kamerayı serbest bırak ve pencereyi kapat
cap.release()
cv2.destroyAllWindows()
