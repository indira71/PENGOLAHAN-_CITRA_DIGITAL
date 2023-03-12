import cv2
import numpy as np
import matplotlib.pyplot as plt

# Baca gambar grayscale
img = cv2.imread('foto9.jpeg', 0)

# Lakukan transformasi Fourier pada gambar
f = np.fft.fft2(img)
fshift = np.fft.fftshift(f)

# Buat filter Ideal Lowpass
rows, cols = img.shape
crow, ccol = rows // 2, cols // 2
radius = 30
mask = np.zeros((rows, cols), np.uint8)
cv2.circle(mask, (ccol, crow), radius, 1, -1)

# Terapkan filter pada spektrum frekuensi
fshift_filtered = fshift * mask

# Geser kembali nol frekuensi ke kiri atas
f_ishift = np.fft.ifftshift(fshift_filtered)

# Lakukan inverse Fourier Transform
img_back = np.fft.ifft2(f_ishift)
img_back = np.abs(img_back)

# Tampilkan gambar asli dan hasil filter
plt.subplot(121), plt.imshow(img, cmap='gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(img_back, cmap='gray')
plt.title('Ideal Lowpass Filtered Image'), plt.xticks([]), plt.yticks([])
plt.show()
