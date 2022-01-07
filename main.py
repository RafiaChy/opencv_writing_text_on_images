import cv2

img = cv2.imread('baboon.jpg', 1)
font = cv2.FONT_HERSHEY_DUPLEX
new_img = cv2.putText(img, 'Write Something', (100, 450), font, 1, (0, 0, 255), 3)
cv2.imshow('New Image', new_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
