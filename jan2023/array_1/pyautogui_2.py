import pyperclip
import pyautogui
import time

# time.sleep(1800)


# class Clicker:

# def continue_clicker(self, x, y, click, accel):


def clicker(x, y, click, accel):
    print(f"예상소요 시간 : {click/accel/9.5 + 15}초")
    bundle = 100
    count = 0
    time.sleep(6)
    pyautogui.moveTo(x, y, duration=3)  # 이동하는 속도 1초 설정
    time.sleep(6)
    cl_start = time.time()
    for i in range(click // bundle):
        pyautogui.click(x, y, clicks=bundle, interval=0.001)
        # if args[0] and args[1]:
        #     pyautogui.click(args[0], args[1], clicks=bundle, interval=0.001)
        #     count += bundle
        # if args[2] and args[3]:
        #     pyautogui.click(args[2], args[3], clicks=bundle, interval=0.001)
        #     count += bundle
        count += bundle
        time.sleep(bundle / 10 / accel)
        end = time.time()
        print(f"✨🖱️✨ 클릭:{count}번    소요시간: {end-cl_start:3f}")
    for i in range(click % bundle):
        pyautogui.click(x, y, clicks=1, interval=0.001)
    count += click % bundle
    cl_end = time.time()
    print(f"✨🖱️✨ 클릭:{count}번    소요시간: {cl_end-cl_start:3f}")


def continuos_clicker(x, y, click, accel, x1, y1, x2, y2):
    print(f"예상소요 시간 : {click * 0.0615}초")
    count = 0
    time.sleep(6)
    pyautogui.moveTo(x, y, duration=3)  # 이동하는 속도 1초 설정
    time.sleep(6)
    cl_start = time.time()
    for _ in range(click // 3 // accel):
        pyautogui.click(x, y, clicks=accel, interval=0.001)
        pyautogui.click(x1, y1, clicks=accel, interval=0.001)
        pyautogui.click(x2, y2, clicks=accel, interval=0.001)
        count += 3 * accel
        if count % 100 == 0:
            cl_end = time.time()
            print(f"✨🖱️✨ 클릭:{count}번    소요시간: {cl_end-cl_start:3f}")

    cl_end = time.time()
    print(f"✨🖱️✨ 클릭:{count}번    소요시간: {cl_end-cl_start:3f}")


def tracker():
    while True:
        time.sleep(0.1)
        print(pyautogui.position())


# 마우스가 해상도 영역을 벗어나면 발생하는 오류를 끔 (특정 환경에서 오류 발생하는 경우 사용)
# pyautogui.FAILSAFE = False
# pyautogui.moveTo(200, 200)  # 화면 해상도의 가로 200, 세로 200 픽셀 위치로 마우스 이동
# pyautogui.click(660, 185)  # 특정 위치에 마우스 클릭 (순간이동하여 클릭함)
# pyautogui.rightClick(560, 172)  # 특정 위치에 마우스 우클릭 (순간이동하여 클릭함)
# pyautogui.moveTo(500, 500, duration=1)  # 이동하는 속도 1초 설정
# pyautogui.click()  # 현재 마우스 커서 위치에서 마우스 클릭
# clicker()
# while True:
#     time.sleep(0.1)
#     print(pyautogui.position())


# pyautogui.typewrite("apple")  # 텍스트 입력
# # 한글 입력시 pyautogui.typewrite('사과') 로 하면 unicode 한글은 입력이 안됨.
# # 아래와 같이 클립보드에 복사해서 붙여넣기 하는 방식으로 진행

# pyperclip.copy("사과")
# pyautogui.hotkey("cmd", "v")

# pyautogui.hotkey(
#     "alt", "f4"
# )  # 단축키 입력 ('esc',  'enter', 'ctrl', 'tab' 등 한 개 또는 복수 키 입력)
# pyautogui.typewrite(["enter"])  # 이렇게 키 입력할 수도 있음

# # 윈도우키를 누르고 있는 상태에서 왼쪽 방향키 짧게 누르고 윈도우키를 뗌
# pyautogui.keyDown("win")
# pyautogui.press("left")
# time.sleep(1.5)
# pyautogui.keyUp("win")
# time.sleep(0.5)

# time.sleep(10)  # 10초 대기 (클릭 후 화면이 뜨기까지 등 반응시간 대기)

# fw = pyautogui.getActiveWindow()
# fw.close()  # 현재 활성화 상태인 창 닫기
if __name__ == "__main__":
    # tracker()

    clicker(360, 340, 20000, 1.55)
    # continuos_clicker(419, 387, 30000, 2, 330, 319, 466, 520)
