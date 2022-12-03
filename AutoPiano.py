# NullUsxr 2022
import pyautogui as gui
import time
class Clr:
    fg = '\033[7m'
    success = '\033[92m'
    stat = '\033[96m'
    info = '\033[93m'
    error = '\033[91m'
    endc = '\033[0m'
def play(song):
    print(f"{Clr.stat}[ALERT]{Clr.endc} Playing song!")
    time.sleep(5)
    i = 0
    while i < len(song):
        if song[i] == "[":
            i += 1
            gui.PAUSE = 0
        elif song[i] == "]":
            i += 1
            gui.PAUSE = delay
        elif song[i] == " ":
            time.sleep(pause)
            print(f"{Clr.info}[INFO]{Clr.endc} Paused")
            i += 1
        elif song[i] == "|":
            time.sleep(longpause)
            print(f"{Clr.info}[INFO]{Clr.endc} Long Paused")
            i += 1
        else:
            gui.typewrite(song[i])
            print(f"{Clr.info}[INFO]{Clr.endc} Played note", "{}/{}".format(i, len(song)))
            i += 1
while 1 == 1:
    print(f"{Clr.fg}NullUsxr's AutoPiano{Clr.endc}")
    try:
        pause = float(input("Pause> "))
        longpause = float(input("Long Pause> "))
        delay = float(input("Delay> "))
        gui.PAUSE = delay
        play(input("Song> "))
        print(f"{Clr.success}[SUCCESS]{Clr.endc} Finished playing song!")
    except ValueError:
        print(f"{Clr.error}[ERROR]{Clr.endc} Invalid number!")
        pass
