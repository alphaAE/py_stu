import cv2

img = cv2.imread("./img.jpg")

cv2.imshow("Demo", img)

cv2.waitKey(0)
cv2.destroyALLwindows()

cv2.imwrite("./img2.jpg", img)