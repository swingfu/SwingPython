while True:
	unit = str.upper(input("Please select the source unit. Type 'F' for Fahrenheit or type 'C' for Celsius: "))
	if unit == 'C':
		number = float(input("Please input the temperature as Celsius: "))
		result = number * 9 / 5 + 32
		print(round(result, 2))
		break
	elif unit == 'F':
		number = float(input("Please input the temperature as Fahrenheit: "))
		result = 5 * (number - 32) / 9
		print(round(result, 2))
		break
	elif unit == 'Q':
		print('Goodbye.')
		break
	else:
		print('Invalid option.')


