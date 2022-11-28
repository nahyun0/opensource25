## 서로 동일 크기, 흑백 저장 change1, change2 로 각각 저장 

import cv2


orign = cv2.imread('img1.jpg')
change = cv2.imread('img2.jpg')

orign_resize = cv2.resize(orign , dsize=(500,500), interpolation=cv2.INTER_AREA)


change_img_color1 = cv2.cvtColor(orign_resize, cv2.COLOR_BGR2GRAY) pyt


change_resize = cv2.resize(change , dsize=(500,500), interpolation=cv2.INTER_AREA)

change_img_color2 = cv2.cvtColor(change_resize, cv2.COLOR_BGR2GRAY) 
