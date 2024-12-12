#! /home/mzamith/Apps/anaconda3/bin/python
import os
import sys
config = sys.argv[1]
density = 0.01
while density <= 0.9:
    print('\n\t\t\033[1;31;48m *--> PID: ', os.getpid(), '\033[1;33;48m')

    cmd = './TModelCA++ {1} {0:.2f}'.format(density, config)
    os.system(cmd)
    density = density + 0.01