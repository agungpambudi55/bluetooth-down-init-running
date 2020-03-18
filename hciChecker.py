'''
Created on Mar 2020
Agung Pambudi <agung.pambudi5595@gmail.com>
'''

import os
import re
import time
import subprocess

os.system('chmod +x /home/<username>/<your directory>/bluetoothResetFirmware.sh')

while True:
    os.system('clear')
    os.system('hciconfig')
        
    if re.findall('DOWN INIT RUNNING', subprocess.getoutput('hciconfig')):
        os.system('/home/<username>/<your directory>/./bluetoothResetFirmware.sh')

    time.sleep(1)
