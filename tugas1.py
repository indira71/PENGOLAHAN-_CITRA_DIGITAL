import cv2

img = cv2.imread("lena.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow("Gambar lenna Original", img)
cv2.imshow("Gambar lenna Grayscale", gray)

cv2.waitKey(0)
cv2.destroyAllWindows()