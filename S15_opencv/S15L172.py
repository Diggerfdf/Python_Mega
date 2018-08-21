import cv2

# Options: -1 is color with Alpha Channels. 0 is gray scale. 1 is RGB
img = cv2.imread("galaxy.jpg", 0)

print(type(img))
print(img)
print(img.shape)
print(img.ndim)

resized_image = cv2.resize(img, (int(img.shape[1]/2), int(img.shape[0]/2)))

cv2.imshow("Galaxy", resized_image)
cv2.imwrite("Galaxy_resized.jpg", resized_image)
cv2.waitKey(0)  # milliseconds
cv2.destroyAllWindows



# img2 = cv2.imread("galaxy.jpg", 1)
# print(img2)
# print(img2.shape)
