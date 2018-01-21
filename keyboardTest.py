import keyboard
def navigate(e):
	for code in keyboard._pressed_events:
		if code == 30 :
			print('LEFT')
		elif code == 31:
			print('BACK')
		elif code == 32:
			print('RIGHT')
		elif code == 17:
			print('FRONT')


	#if keyboard.is_pressed(30):
	#	print('LEFT')
	#elif keyboard.is_pressed(31):
		#print('BACK')
	#elif keyboard.is_pressed(32):
		#print('RIGHT')
	#elif keyboard.is_pressed(17):
		#print('FRONT')

keyboard.hook(navigate)
keyboard.wait()