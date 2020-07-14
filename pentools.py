#!/usr/bin/env python

import platform
import sys
import subprocess

Banner = '''
                              
 *********       **************   ******        ***  *****************      *********            *********       ****            **************
 ***    *****    **************   *** ***       ***  *****************   ***************      ***************    ****           **************
 ***       ****  ***              ***  ***      ***        *****        ***           ***    ***           ***   ****           ****
 ***       ****  ***              ***   ***     ***        *****       ***             ***  ***             ***  ****           **************
 ***    *****    **************   ***    ***    ***        *****       ***             ***  ***             ***  ****           **************
 ********        **************   ***     ***   ***        *****       ***             ***  ***             ***  ****                   ******
 ***             ***              ***      ***  ***        *****        ***           ***    ***           ***   ****                   ******
 ***             **************   ***       *******        *****         ***************      ***************    *************   *************
 ***             **************   ***        ******        *****            *********            ********        *************  *************
                   
'''
print(Banner)

OS = platform.system()

if OS == 'Windows':
    sys.exit("Sorry :(, but Pentools is only compatible with Unix based Systems.")
elif OS == 'Linux':
    pass
else :
    print("Unidentifield OS....")
    r = chr(input(' Pentools is only compatible with Linux System Operation, continue? (y)'))
    if r.upper != 'Y':
        sys.exit()

subprocess.run("sudo bash ./core")
