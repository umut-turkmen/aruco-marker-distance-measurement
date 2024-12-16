import cv2
import numpy as np

# Satranç tahtası boyutları (9x6)
chessboard_size = (9, 6)  # Satranç tahtasındaki kare sayısı (9x6)

# Görselin boyutlarını ayarla
square_size = 50  # Her bir karenin boyutu (px)

# Satranç tahtasını oluştur
objp = np.zeros((chessboard_size[0] * chessboard_size[1], 3), np.float32)
objp[:, :2] = np.mgrid[0:chessboard_size[0], 0:chessboard_size[1]].T.reshape(-1, 2)

# 3D ve 2D noktaları saklamak için listeler
obj_points = []  # 3D noktalara karşılık gelen dünya koordinatları
img_points = []  # 2D noktalara karşılık gelen görüntü koordinatları

# Satranç tahtasını tespit etmek için video kaynağını aç
cap = cv2.VideoCapture(1)  # Logitech kamera için 1

while True:
    ret, frame = cap.read()
    if not ret:
        print("Kare alınamadı!")
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Satranç tahtasını tespit et
    ret, corners = cv2.findChessboardCorners(gray, chessboard_size, None)

    if ret:
        # Geçici noktaları kaydet
        obj_points.append(objp)
        img_points.append(corners)

        # Satranç tahtasının köşelerini çiz
        cv2.drawChessboardCorners(frame, chessboard_size, corners, ret)
        print("Satranç tahtası tespit edildi!")
    else:
        print("Satranç tahtası tespit edilemedi.")

    # Görüntüyü göster
    cv2.imshow("Satranç Tahtası", frame)

    # 'q' tuşuna basıldığında çık
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Kamerayı serbest bırak ve pencereyi kapat
cap.release()
cv2.destroyAllWindows()

# Kalibrasyon işlemini yap
if len(obj_points) > 0 and len(img_points) > 0:
    ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(obj_points, img_points, gray.shape[::-1], None, None)
    print("Kalibrasyon Başarılı!")
    print("Kamera Matrisini:", mtx)
    print("Distorsiyon Parametreleri:", dist)
else:
    print("Yeterli görüntü alınamadı. Lütfen daha fazla açıdan görüntü alın.")
