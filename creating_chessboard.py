import cv2
import numpy as np

# Satranç tahtası boyutları (9x6)
chessboard_size = (9, 6)  # Satranç tahtasındaki kare sayısı (9x6)

# Görselin boyutlarını ayarla
square_size = 50  # Her bir karenin boyutu (px)

# Satranç tahtasını oluştur
board_width = chessboard_size[0] * square_size
board_height = chessboard_size[1] * square_size
board = np.zeros((board_height, board_width), dtype=np.uint8)

# Kareleri çiz
for i in range(chessboard_size[1]):
    for j in range(chessboard_size[0]):
        if (i + j) % 2 == 0:
            cv2.rectangle(board, (j * square_size, i * square_size),
                          ((j + 1) * square_size, (i + 1) * square_size),
                          (255), -1)  # Beyaz kareler

# Görseli kaydet
cv2.imwrite("chessboard.png", board)

# Görseli göster (isteğe bağlı)
cv2.imshow("Satranç Tahtası", board)
cv2.waitKey(0)
cv2.destroyAllWindows()
