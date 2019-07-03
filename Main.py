# -*- coding: utf-8 -*-
import pyautogui
import time
from time import sleep
import pynput
from pynput import keyboard

import DetectWithCUDA

Going = False
#Going = True
while Going:
    s = time.time()
    DetectWithCUDA.Running()
    f =time.time()
    print(f - s)
