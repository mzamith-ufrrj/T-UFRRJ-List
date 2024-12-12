#!/usr/bin/python3.8
import os
import time
import sys
print('Hello, I am ', os.getpid())
print(sys.argv[1])
time.sleep(int(sys.argv[1]))
print('End the game')