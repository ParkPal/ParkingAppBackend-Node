from envirophat import motion

class CarSensor:

	def is_occupied(self):
		tmp = motion.magnetometer()
		if tmp[1] > 0:
			# print("Car detected...")
			return True
		else:
			return False
