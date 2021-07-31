import pyautogui
import time


class HoursFiller:
    cx, cy = 0, 0
    interval = 1
    day = 0

    def __init__(self):
        self.cx, self.cy = pyautogui.position()

    def move_mouse_relative(self, x, y):
        self.cx += x
        self.cy += y
        pyautogui.moveTo(self.cx, self.cy)

    def perform_sequence(self):
        if self.day >= 5:
            pyautogui.click()
            self.move_mouse_relative(0, 82)
            self.day = 0

        self.day += 1
        pyautogui.click()
        pyautogui.write('0900')
        self.move_mouse_relative(-70, 0)
        pyautogui.click()
        time.sleep(self.interval)
        pyautogui.click()
        pyautogui.write('1800')
        self.move_mouse_relative(70, 41)
        pyautogui.click()
        time.sleep(self.interval)


def main():
    time.sleep(5)
    print('starting')

    hf = HoursFiller()
    for i in range(20):
        hf.perform_sequence()

    print('finished')


if __name__ == '__main__':
    main()

