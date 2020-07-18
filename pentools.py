#!/usr/bin/env python3

import platform
import sys
import subprocess

Banner = '''

 *******    ********  ****       **  ************   ********        ********     **         ********
 **    ***  **        ** **      **       **      ***      ***    ***      ***   **         ***
 **    ***  **        **  **     **       **     ***        ***  ***        ***  **         ***
 ******     ********  **   **    **       **     ***        ***  ***        ***  **         ********
 **         **        **    **   **       **     ***        ***  ***        ***  **              ***
 **         **        **     **  **       **      ***      ***    ***      ***   **              ***
 **         ********  **      *****       **        ********        ********     *********  ********

'''
print(Banner)

OS = platform.system()

if OS == 'Windows':
    pass
    # sys.exit("Sorry :(, but Pentools is only compatible with Unix based Systems.")
elif OS == 'Linux':
    pass
else:
    print("Unidentifield OS....")
    r = chr(
        input(' Pentools is only compatible with Linux System Operation, continue? (y)'))
    if r.upper != 'Y':
        sys.exit()

subprocess.run(["sudo","bash", "./core.sh"])

opt = None
while opt != 1 and opt != 2:
    try:
        opt = int(input('''Which instalation mode do you prefer?
1. Essentials Tools
2. Complete
Option: '''))

    except ValueError:
        opt = None

if opt == 1:
    subprocess.run(["sudo","bash", "./installations_modes/essentials.sh"])
elif opt == 2:
    subprocess.run(["sudo","bash", "./installations_modes/complete.sh"])
