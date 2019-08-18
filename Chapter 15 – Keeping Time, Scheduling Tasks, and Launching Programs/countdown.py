#! python3
# countdown.py - A simple countdown script.

import time, subprocess

timeLeft = 10
while timeLeft > 0:
    print(timeLeft, end="")
    time.sleep(1)
    timeLeft -= 1

subprocess.Popen(['C:/Program Files (x86)/VideoLAN/VLC/vlc.exe', 'C:\\Windows\\Media\\Alarm01.wav'], shell=True)