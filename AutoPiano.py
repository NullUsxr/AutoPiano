# Auto-Piano
# NullUsxr 2022
import pyautogui as gui
import time as tm


def play(song):
    print("[ALERT] Now playing song")
    tm.sleep(5)
    counter = 0
    clockspeed = gui.PAUSE
    while counter < len(song):
        for i in range(10):  # Parse most unneeded text
            if counter < len(song):  # Prevent string index out of range crash
                if song[counter] == "[":
                    gui.PAUSE = 0
                    counter = counter + 1
            if counter < len(song):
                if song[counter] == " ":
                    tm.sleep(pause)
                    counter = counter + 1
                    print("[INFO] Paused")
            if counter < len(song):
                if song[counter] == "|":
                    tm.sleep(longpause)
                    counter = counter + 1
                    print("[INFO] Long Paused")
            if counter < len(song):
                if song[counter] == "]":
                    gui.PAUSE = clockspeed
                    counter = counter + 1
        if counter < len(song):
            gui.press(song[counter])
            counter = counter + 1
            print("[INFO] Played", counter, "/", len(song))


while 1 == 1:
    print("NullUsxr's AutoPiano Program")
    pause = float(input("Pause: "))
    longpause = float(input("Long Pause: "))
    gui.PAUSE = float(input("Playback Speed: "))
    play(input("Song: "))
    print("[ALERT] Finished playing song")
