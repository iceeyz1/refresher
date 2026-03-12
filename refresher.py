import webbrowser
import pyautogui
import time

url = input("Enter Website Link: ")
refreshmenge = int(input("Refresh count (e.g. 10): "))
refreshsleep = int(input("Refresh delay (1 equals 1 second): "))


webbrowser.open(url)
time.sleep(2)

for i in range(refreshmenge):
    pyautogui.press("f5")
    time.sleep(refreshsleep)

print("Finished! (This automatically closes in 5 Seconds.)")
time.sleep(5)