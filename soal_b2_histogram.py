import os
import cv2
import matplotlib.pyplot as plt
import numpy as np

# Cari citra di folder saat ini (Colab) atau path lokal
img_name = '2022-Ferrari-Daytona-SP3-009-1600.jpg'
if not os.path.exists(img_name):
    img_name = r'D:\Tugas Kuliah\Visi Komputer\2022-Ferrari-Daytona-SP3-009-1600.jpg'

# Muat citra berwarna
img = cv2.imread(img_name)

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
