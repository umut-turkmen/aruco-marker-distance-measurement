import numpy as np
import cv2
from cv2 import aruco

# Hazır Aruco sözlüğünü al
aruco_dict = aruco.getPredefinedDictionary(aruco.DICT_4X4_50)

# Marker 1 oluştur
marker_id1 = 1  # ID değeri
marker_size = 200  # Marker boyutu (piksel)
marker_img1 = np.zeros((marker_size, marker_size), dtype=np.uint8)
aruco.generateImageMarker(aruco_dict, marker_id1, marker_size, marker_img1, 1)

# Marker 2 oluştur
marker_id2 = 2  # ID değeri
marker_img2 = np.zeros((marker_size, marker_size), dtype=np.uint8)
aruco.generateImageMarker(aruco_dict, marker_id2, marker_size, marker_img2, 1)

# Marker görsellerini kaydet
cv2.imwrite("marker1.png", marker_img1)
cv2.imwrite("marker2.png", marker_img2)

print("Marker görselleri oluşturuldu: marker1.png ve marker2.png")



