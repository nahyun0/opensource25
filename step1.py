import pyautogui
from PIL import ImageChops
import cv2

while True:
    result = pyautogui.confirm('틀린 그림 찾기', buttons=['시작','종료'])
    if result == '종료':
        break # 프로그램 종료

    width, height = 956, 763
    y_pos = 45

    left = pyautogui.screenshot(region=(0,y_pos,width, height)) #왼쪽 이미지
    right = pyautogui.screenshot(region=(963, y_pos, width, height)) #오른쪽 이미지
    diff = ImageChops.difference(left, right) #이미지비교
    diff.save('gamescreen.jpg')

    # 파일 생성 대기
    while not os.path.exists('gamescree.jpg'):
        time.sleep(1)

    diff_img = cv2.imread('gamescreen.jpg')
    gray = cv2.cvtColoer(diff_img, cv2.COLOR_BGR2GRAY)
    contours,_= cv2.findContours(gray, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    COLOR = (0, 200, 0)
    for cnt in contours:
        if cv2.contourArea(cnt) > 100:
            x, y, width, height = cv2.boundingRect(cnt)
            click_x= x + (width // 2)
            click_y= y + (height // 2) + y_pos
            pyautogui.moveTo(click_x, click_y, duration=0.1)
            pyautogui.click(click_x, click_y)

    
    
