#### Edge Detection in an image 
import cv2

img = cv2.imread('open_cv/image/pikachu.jpeg')

# We are using the Canny Edge Detection Algorithm here
# No need to dive deep into explanation over here
edges = cv2.Canny(img, 100, 200)
#cv2.imwrite('result.jpg' , edges)
cv2.imshow('Original Image', img)
cv2. imshow('Rotated Image', edges)
cv2.waitKey(0)