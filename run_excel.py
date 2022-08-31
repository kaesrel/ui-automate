import time
from ui_auto import UiAuto

# "C:\Program Files\Microsoft Office\root\Office16\EXCEL.EXE"
window_name = "Example.xlsx"
path = "C:\\Program Files\\Microsoft Office\\root\\Office16"
program = "EXCEL.EXE"
arg = "Example.xlsx"

ui = UiAuto(window_name=window_name, path=path, program=program, arg=arg)

ui.focus_window()

# x=64, y=306
ui.fill_at(64, 306, 'hello', isrelative=True)

ui.fill_next('hi')
ui.fill_next("=1+2+5")
ui.next()
ui.press_hotkey("down")
ui.fill_current("okay")

ui.click(64, 306, isrelative=True)

# select 3 cells
ui.press_hotkey('shiftleft', 'shiftright', "right")
ui.press_hotkey('shiftleft', 'shiftright', "right")

# copy selected cells
ui.press_hotkey("ctrl", "c")

ui.press_hotkey("down")
ui.press_hotkey("down")
ui.press_hotkey("down")

# paste cells
ui.press_hotkey("ctrl", "v")

ui.press_hotkey("esc")