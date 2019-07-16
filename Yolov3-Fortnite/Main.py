# -*- coding: utf-8 -*-
import time
from DarknetUtilities import Detection

Running = True
while Running:
    s = time.time()
    Detection.Running()
    f =time.time()
    print(f - s)