'''
Created on Mar 2020
Agung Pambudi <agung.pambudi5595@gmail.com>

Example, I have a problem with bluetooth when the program runs after adapter.start(),
sometimes the status changes from UP RUNNING to DOWN INIT RUNNING,
then stuck or freezes in that status.
'''

import pygatt

def checkDevice():
	try:
		adapter = pygatt.GATTToolBackend(hci_device='hci0') # Check hciconfig on terminal
		adapter.start()

		for discover in adapter.scan(run_as_root=True, timeout=5):
			if discover['name'] == '<bluetooth name>':
				device = adapter.connect(discover['address'])
				print('Connected with device')
				device.disconnect()

	except:
		print('Something went wrong with the bluetooth, waiting for bluetooth firmware to reset until status is UP RUNNING again')
		checkDevice()
	
	finally:
		adapter.stop()

if __name__ == '__main__':
	checkDevice()