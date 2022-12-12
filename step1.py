import pyautogui
from PIL import ImagaeChops

width, height = 956, 763
y_pos = 45

left = pyautogui.screenshot(region=(0,y_pos,width, height)) #왼쪽 이미지
right = pyautogui.screenshot(region=(963, y_pos, width, height)) #오른쪽 이미지

diff = ImageChops.difference(left, right) #이미지비교
diff.save('gamescreen.jpg')