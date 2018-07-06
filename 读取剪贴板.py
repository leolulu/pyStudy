import win32con
import win32clipboard

#读取剪贴板
win32clipboard.OpenClipboard()
t = win32clipboard.GetClipboardData(win32con.CF_TEXT)
win32clipboard.CloseClipboard()
print(t)
