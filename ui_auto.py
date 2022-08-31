import pyautogui, time, sys, os, subprocess

class UiAuto:
    def __init__(self, window_name, path="", program="", arg=[]):
        self.window_name = window_name
        self.program = program
        self.path = path
        self.arg=arg

        # print(window_name, len(pyautogui.getWindowsWithTitle(self.window_name)))
        if len(pyautogui.getWindowsWithTitle(self.window_name)) == 0:
            self.start_program()

        self.window = pyautogui.getWindowsWithTitle(self.window_name)[0]

    def start_program(self):
        if self.path == '':
            self.path = '.'
        subprocess.Popen([f'{self.path}\\{self.program}', self.arg])
        time.sleep(1)

    def focus_window(self):
        self.window.minimize()
        # self.window.maximize()
        self.window.restore()
        time.sleep(2)

    def focus_and_maximize_window(self):
        self.window.minimize()
        self.window.maximize()
        time.sleep(2)

    def fill_at(self, x, y, content, isrelative=False):
        # pyautogui.click(x, y)
        self.click(x, y, isrelative)
        pyautogui.typewrite(content)

    def fill_current(self, content):
        pyautogui.typewrite(content)    

    def fill_next(self, content):
        pyautogui.typewrite(["tab"])
        pyautogui.typewrite(content)

    def press_hotkey(self, *keys):
        pyautogui.hotkey(*keys)

    def keyDown(self, key):
        pyautogui.keyDown(key)

    def keyUp(self, key):
        pyautogui.keyUp(key)

    def next(self):
        pyautogui.hotkey('tab')

    def previous(self):
        pyautogui.hotkey('shift', 'tab')

    def click(self, x=-1, y=-1, isrelative=False):
        if x<0 or y<0:
            x,y = pyautogui.position()

        if isrelative:
            x_, y_ = self.window.topleft
            x += x_
            y += y_

        pyautogui.click(x,y)

    def double_click(self, x=-1, y=-1, isrelative=False):
        if x<0 or y<0:
            x,y = pyautogui.position()

        if isrelative:
            x_, y_ = self.window.topleft
            x += x_
            y += y_

        pyautogui.doubleClick(x,y)