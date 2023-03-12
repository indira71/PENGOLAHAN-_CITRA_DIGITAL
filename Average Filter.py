import cv2
import numpy as np

img = cv2.imread('foto3.jpg')

kernel_size = (5, 5)

kernel = np.ones(kernel_size, np.float32) / (kernel_size[0] * kernel_size[1])

filtered_img = cv2.filter2D(img, -1, kernel)

cv2.imshow('Original Image', img)
cv2.imshow('Filtered Image', filtered_img)
cv2.waitKey(0)
