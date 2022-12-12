import pyautogui
from PIL import ImagaeChops
import cv2

width, height = 956, 763
y_pos = 45

left = pyautogui.screenshot(region=(0,y_pos,width, height)) #왼쪽 이미지
right = pyautogui.screenshot(region=(963, y_pos, width, height)) #오른쪽 이미지

diff = ImageChops.difference(left, right) #이미지비교
diff.save('gamescreen.jpg')

diff_img = cv2.imread('gamescreen.jpg')
gray = cv2.cvtColoer(diff_img, cv2.COLORBGR2GRAY)
contours,= cv2.findContours(gray, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

COLOR = (0, 200, 0)
for cnt in contours:
    if cv2.contourArea(cnt) > 100:
        x, y, width, height = cv2.boundingRect(cnt)
        cv2.rectangle(diff_img, (x,y), (x +width, y + height), COLOR, 2)
        click_x= x + (width // 2)
        click_y= y + (height // 2) + y_pos
        pyautogui.moveTo(click_x, click_y, duration=0.1)
        pyautogui.click(click_x, click_y)

cv2.imshow('diff',diff_img)
cv2.waitkey(0)
cv2.destoryALLWindows()
