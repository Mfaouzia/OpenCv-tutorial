# Resize and Cropping

import cv2
import numpy as np

img = cv2.imread("Ressources/lambo.png")
print(img.shape)
"""
Image Resize
"""

imgResize = cv2.resize(img,(1000, 500))
print(imgResize.shape)

"""
image Cropped
"""
imgCropped = img[0:200, 200:400]

cv2.imshow("Image", img)
cv2.imshow("Image Resize", imgResize)
cv2.imshow("Image Cropped", imgCropped)

cv2.waitKey(0)

