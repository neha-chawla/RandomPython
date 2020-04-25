#!/usr/bin/env python3
import pyautogui

path = "scripts/beeMovie.txt"
script=open(path, 'r')
words = script.read().split()

for word in words:
    pyautogui.write(word)
    pyautogui.press("enter")

