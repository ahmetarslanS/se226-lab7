
import cv2


image = cv2.imread('img.jpg')


cv2.imshow('Original_Image', image)


b, g, r = cv2.split(image)

cv2.imshow("Model Blue Image", b)


cv2.imshow("Model Green Image", g)

cv2.imshow("Model Red Image", r)
print("Press any key to continue")
cv2.waitKey(0)


px = image[100,100]
print("Original version of pixel values")
print(px)

image[100,100] = [178 ,147 ,255]
print("Modified version of pixel values")
print(image[100,100])

cv2.imshow('Modified_Image', image)


image = cv2.merge((b,g,r))

cv2.imshow("Modified_Image",image)
print("Press any key to continue")
cv2.waitKey(0)
