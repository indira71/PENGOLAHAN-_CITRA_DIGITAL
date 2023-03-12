import cv2
from matplotlib import pyplot as plt

img = cv2.imread('foto4.jpeg', 0)

eq_img = cv2.equalizeHist(img)

eq_hist = cv2.calcHist([eq_img], [0], None, [256], [0, 256])

fig, axs = plt.subplots(1, 2, figsize=(10, 5))
axs[0].imshow(img, cmap='gray')
axs[0].set_title('Original Image')
axs[1].imshow(eq_img, cmap='gray')
axs[1].set_title('Equalized Image')
plt.show()

fig, axs = plt.subplots(1, 2, figsize=(10, 5))
axs[0].plot(cv2.calcHist([img], [0], None, [256], [0, 256]))
axs[0].set_title('Original Histogram')
axs[1].plot(eq_hist)
axs[1].set_title('Equalized Histogram')
plt.show()
