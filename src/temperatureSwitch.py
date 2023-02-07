while True:
	unit = input("Please select the source unit. Type 'F' for Fahrenheit or type 'C' for Celsius: ")
	if unit == 'C' or unit == 'c':
		number = int(input("please input the temperature as Celsius: "))
		result = number * 9 / 5 + 32
		print(result)
		break
	elif unit == 'F' or unit == 'f':
		number = int(input("Please input the temperature as Fahrenheit: "))
		result = 5*(number-32)/9
		print(result)
		break
	elif unit == 'Q' or unit == 'q':
		print('goodbye')
		break
	else:
		print('Invalid option')


