import sys
import pyautogui
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import *
from tqdm import tqdm
import time


class MyApp(QWidget):
    def __init__(self):
        super().__init__()

        self.x, self.y, self.delay, self.num_click = 0, 0, 0, 0

        self.start_btn_click()

    def start_btn_click(self):
        self.timer = QTimer()
        self.x = 800
        self.y = 500
        self.delay = 3
        self.routine_number = 3

        self.timer.start(self.delay * 1000)
        self.timer.timeout.connect(self.mouse_click)

    def mouse_click(self):
        pyautogui.click(self.x, self.y)
        self.num_click += 1

        if self.num_click == self.routine_number:
            self.timer.stop()


if __name__ == "__main__":
    # app = QApplications(sys.argv)
    # print("-")
    # ex = MyApp()
    # sys.exit(app.exec_())
    for i in range(100):
        start = time.time()
        end = time.time()
        print(f"{end - start:5f}")
