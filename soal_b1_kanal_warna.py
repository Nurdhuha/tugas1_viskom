import os
import urllib.request
import cv2
import matplotlib.pyplot as plt

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

# OpenCV membaca dalam format BGR, konversi ke RGB untuk matplotlib
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Pisahkan kanal warna
R = img_rgb[:, :, 0]  # Kanal Red
G = img_rgb[:, :, 1]  # Kanal Green
B = img_rgb[:, :, 2]  # Kanal Blue

# Tampilkan 3 sub-plot
fig, axes = plt.subplots(1, 3, figsize=(15, 5))

axes[0].imshow(R, cmap='gray')
axes[0].set_title('Kanal Red', fontsize=12)
axes[0].axis('off')

axes[1].imshow(G, cmap='gray')
axes[1].set_title('Kanal Green', fontsize=12)
axes[1].axis('off')

axes[2].imshow(B, cmap='gray')
axes[2].set_title('Kanal Blue', fontsize=12)
axes[2].axis('off')

plt.suptitle('Pemisahan Kanal Warna (RGB) dalam Grayscale', fontsize=14, y=1.02)
plt.tight_layout()
plt.savefig('output_kanal_warna.png', dpi=150, bbox_inches='tight')
plt.show()
print("output_kanal_warna.png berhasil disimpan!")
