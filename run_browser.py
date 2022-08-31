import time
from ui_auto import UiAuto

window_name = "Google - Google Chrome"
path = "C:\Program Files\Google\Chrome\Application"
program = "chrome.exe"
arg = "http://google.com"

# window_name = "Mozilla Firefox"
# path = "C:\Program Files\Mozilla Firefox"
# program = "firefox.exe"
# arg = "http://google.com"

ui = UiAuto(window_name=window_name, path=path, program=program, arg=arg)

# ui.focus_and_maximize_window()
ui.focus_window()

ui.fill_current('hello')
ui.press_hotkey("enter")
