# ##### Rotating an image
import cv2

img = cv2.imread('open_cv/image/pikachu.jpeg')
rows, cols,_ = img.shape

# # getRotationMatrix2D creates a matrix needed for transformation.
# # We want matrix for rotation w.r.t center to 45 degree without scaling.
M = cv2.getRotationMatrix2D((cols / 2, rows / 2), -90, 1)
res = cv2.warpAffine(img, M, (cols, rows))

#rotate image
result = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
cv2.imshow('result.jpg', result)
cv2.imshow('Original Image', img) 
cv2.imshow('Rotated Image', res)
cv2.waitKey(0)