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