# -*- coding: utf-8 -*-
import time
from time import sleep

import DetectWithCUDA

Going = True
while Going:
    s = time.time()
    DetectWithCUDA.Running()
    f =time.time()
    print(f - s)
