import cv2
import numpy as np
import matplotlib.pyplot as plt

# Baca gambar grayscale
img = cv2.imread('foto8.jpeg', 0)
# Lakukan FFT pada gambar
f = np.fft.fft2(img)
fshift = np.fft.fftshift(f)

# Hitung magnitudo spektrum frekuensi
magnitude_spectrum = 20 * np.log(np.abs(fshift))

# Filter frekuensi rendah
rows, cols = img.shape
crow, ccol = rows // 2, cols // 2
mask = np.zeros((rows, cols), np.uint8)
mask[crow-30:crow+30, ccol-30:ccol+30] = 1
fshift = fshift * mask

# Geser kembali nol frekuensi ke kiri atas
f_ishift = np.fft.ifftshift(fshift)

# Lakukan inverse FFT untuk mendapatkan gambar yang sudah difilter
img_back = np.fft.ifft2(f_ishift)
img_back = np.abs(img_back)

# Tampilkan gambar asli, spektrum frekuensi, dan gambar hasil filter
plt.subplot(131), plt.imshow(img, cmap='gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])
plt.subplot(132), plt.imshow(magnitude_spectrum, cmap='gray')
plt.title('Magnitude Spectrum'), plt.xticks([]), plt.yticks([])
plt.subplot(133), plt.imshow(img_back, cmap='gray')
plt.title('Image after HPF'), plt.xticks([]), plt.yticks([])
plt.show()
