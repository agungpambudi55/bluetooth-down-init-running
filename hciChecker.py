import os
import re
import subprocess

while True:
    os.system('clear')
    os.system('hciconfig')
        
    if re.findall('DOWN INIT RUNNING', subprocess.getoutput('hciconfig')):
        os.system('/home/<username>/<your directory>/./bluetoothResetFirmware.sh')
