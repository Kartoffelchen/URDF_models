import cv2

path = 'checker_blue3.jpg'

srcImg = cv2.imread(path)

dim = (512,512)
resizedImg = cv2.resize(srcImg, dim, interpolation = cv2.INTER_AREA)
cv2.imwrite('checker_blue3.png',resizedImg)
