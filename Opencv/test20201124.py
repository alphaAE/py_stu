
import numpy
import cv2

img = cv2.imread("./Opencv/img.jpg")

cv2.imshow("Demo", img)

cv2.waitKey(0)
cv2.destroyAllWindows()

# cv2.imwrite("./img2.jpg", img)
