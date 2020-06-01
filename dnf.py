import win32gui
import win32con
import pyautogui
import win32api
import time
import ctypes
import win32com.client
dm = win32com.client.Dispatch('dm.dmsoft')  #调用大漠插件

if __name__=='__main__':
    hWnd = win32gui.FindWindow(None, "地下城与勇士")
    win32gui.SetForegroundWindow(hWnd)
    win32gui.SetActiveWindow(hWnd)
    time.sleep(1.0)
    dm.keypress(65)  # 游戏中钓鱼快捷键键位码
    time.sleep(0.1)
    dm.keyup(65)











