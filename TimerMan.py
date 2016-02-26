#!/usr/bin/env python3
# author: camabeh

from screenshoter import Screenshoter
import pyautogui
import time


class TimberMan:
    def __init__(self):
        self.s = Screenshoter()
        self.img = None

    def get_data(self):
        left = self.img.crop((0, 0, 150, 50))
        right = self.img.crop((330, 0, 480, 50))

        return left, right

    def make_screenshot(self):
        self.img = self.s.grab((240, 580, 720, 630))

    @staticmethod
    def is_end(img):
        rgb = img.getpixel((240, 5))
        return rgb == (83, 49, 29)

    @staticmethod
    def is_branch(branch_img):
        rgb = branch_img.getpixel((80, 20))

        return rgb == (163, 151, 63)

    @staticmethod
    def click(direction):
        if direction == 'left':
            pyautogui.click(200, 500)
        else:
            pyautogui.click(600, 500)

    @staticmethod
    def press(direction):
        pyautogui.press(direction)

    def run(self):
        # Start at menu, it will start itself
        pyautogui.click(500, 800)

        while True:
            time.sleep(0.03)
            self.make_screenshot()

            if TimberMan.is_end(self.img):
                print('end')
                break
            else:
                left, right = self.get_data()

                if TimberMan.is_branch(left):
                    print('left')
                    TimberMan.press('right')

                elif TimberMan.is_branch(right):
                    TimberMan.press('left')
                    print('right')
                else:
                    TimberMan.press('left')
                    print('none')


if __name__ == '__main__':
    timberMan = TimberMan()
    timberMan.run()
