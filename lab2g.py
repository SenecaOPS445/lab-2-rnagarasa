#!/usr/bin/env python3

'''
Author: Rajkumar Nagarasa
Author ID: 071788145
Date Created: 2025/01/24
'''

import sys

if len(sys.argv) == 2:
    timer = int(sys.argv[1])
else:
    timer = 3


while timer != 0:
    print(timer)
    timer = timer - 1


print('blast off!')