import cv2
from cv2 import aruco
import numpy as np

# ArUco marker için gerekli olan parametreler
marker_length = 5.0  # Marker uzunluğu (cm cinsinden)
focal_length = 631.73474764  # Kalibrasyon matrisinden alınan focal length (piksel)
camera_matrix = np.array([[631.73474764, 0, 230.30676439],  # Kameranın matris değerleri
                          [0, 619.38636725, 228.45809363],
                          [0, 0, 1]])

distortion_coefficients = np.array([-0.27870423, 1.19117131, 0.01317574, -0.02699152, -1.48986633])  # Distorsiyon parametreleri

# ArUco dictionary ve parameters
aruco_dict = aruco.getPredefinedDictionary(aruco.DICT_4X4_50)  # Düzgün şekilde dictionary'yi tanımladık
parameters = cv2.aruco.DetectorParameters()  # Detector parametreleri

# Kamerayı başlatıyoruz (Logitech kamera için)
cap = cv2.VideoCapture(1)  # Eğer birden fazla kamera bağlıysa, doğru ID'yi seçin (0, 1, 2,...)

while True:
    ret, frame = cap.read()

    if not ret:
        print("Kamera açılmadı!")
        break

    # Görüntüdeki ArUco markerlarını tespit et
    corners, ids, rejectedImgPoints = cv2.aruco.detectMarkers(frame, aruco_dict, parameters=parameters)

    if len(corners) > 0:  # Eğer markerlar tespit edildiyse
        frame = cv2.aruco.drawDetectedMarkers(frame, corners, ids)

        # Markerların köşe noktalarını elde et
        for i in range(len(corners)):
            corner = corners[i][0]
            # Mesafe hesaplama: Her marker'ın bir köşesinin koordinatlarını alıyoruz
            if i == 1:  # İkinci markerı tespit edince
                p1 = corners[0][0][0]  # İlk marker köşesi
                p2 = corners[1][0][0]  # İkinci marker köşesi
                distance_pixels = np.linalg.norm(p2 - p1)  # Piksel cinsinden mesafe hesaplama

                # Piksel mesafesini cm'ye çeviriyoruz
                distance_cm = (distance_pixels * marker_length) / focal_length  # Piksel mesafesini cm'ye çevir
                cv2.putText(frame, f"Distance: {distance_cm:.2f} cm", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    # Kamerayı ekranda göster
    cv2.imshow("Frame", frame)

    # 'q' tuşuna basarak çıkış yapabilirsiniz
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
