import cv2
path = 'texture_map.png'
srcImg = cv2.imread(path)
imgGray = cv2.cvtColor(srcImg,cv2.COLOR_RGB2GRAY)
cv2.imwrite('texture_map2.png',imgGray)
