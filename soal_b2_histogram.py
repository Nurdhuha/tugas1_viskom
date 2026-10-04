import os
import urllib.request
import cv2
import matplotlib.pyplot as plt
import numpy as np

IMAGE_NAME = '2022-Ferrari-Daytona-SP3-009-1600.jpg'
RAW_URL = 'https://raw.githubusercontent.com/Nurdhuha/tugas1_viskom/main/2022-Ferrari-Daytona-SP3-009-1600.jpg'

# Cek ketersediaan file citra (lokal / Colab)
if not os.path.exists(IMAGE_NAME):
    local_fallback = r'D:\Tugas Kuliah\Visi Komputer\2022-Ferrari-Daytona-SP3-009-1600.jpg'
    if os.path.exists(local_fallback):
        IMAGE_NAME = local_fallback
    else:
        print(f"Mengunduh {IMAGE_NAME} dari GitHub...")
        urllib.request.urlretrieve(RAW_URL, IMAGE_NAME)

# Muat citra berwarna
img = cv2.imread(IMAGE_NAME)

# Konversi ke Grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Hitung histogram
histogram = cv2.calcHist([gray], [0], None, [256], [0, 256])

# Plot histogram
plt.figure(figsize=(10, 5))
plt.plot(histogram, color='black', linewidth=1)
plt.fill_between(range(256), histogram.flatten(), alpha=0.3, color='steelblue')
plt.title('Histogram Intensitas Grayscale', fontsize=14)
plt.xlabel('Nilai Intensitas Piksel (0-255)', fontsize=11)
plt.ylabel('Jumlah Piksel', fontsize=11)
plt.xlim([0, 255])
plt.grid(axis='y', alpha=0.3)
plt.tight_layout()
plt.savefig('output_histogram.png', dpi=150, bbox_inches='tight')
plt.show()
print("output_histogram.png berhasil disimpan!")
