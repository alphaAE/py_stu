import cv2
import matplotlib.pyplot as plt
import numpy as n

img_cat = cv2.imread('./Opencv/cat.jpg')
img_dog = cv2.imread('./Opencv/dog.jpg')

img_cat = cv2.resize(img_cat, (500, 400))
img_dog = cv2.resize(img_dog, (500, 400))

res = img_cat // 2 + img_dog // 2

cv2.imshow('image', res)

cv2.waitKey(0)
cv2.destroyAllWindows()
