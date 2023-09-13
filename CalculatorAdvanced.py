# from colorama import init
# from colorama import Fore, Back, Style

def main():

	# print(Fore.BLACK) 
	# print(Back.CYAN)

	operation()

	# print(Back.RED)

	number()

	# print(Back.YELLOW)


	if what == "+":
		print("Результат:" + str(a + b))

	elif what == "-":
		print("Результат:" + str(a - b))

	elif what == "*":
		print("Результат:" + str(a * b))

	elif what == "/":
		try:
			print("Результат:" + str(a / b))
		except ZeroDivisionError:
			print("Нельзя делить на ноль!")
			main()

	elif what == "^":
		print("Результат:" + str(pow(a, b)))

	restart()

def operation():
	global what
	accepted = ['+', '-', '*', '/', '^']
	what = input("\nВыберите знак (+, -, *, /, ^): \n")
	
	if what not in accepted:
		operation()

def number():
	try:
		global a
		global b
		a = float(input("Введите первое число: \n"))
		b = float(input("\nВведите второе число: \n"))
	except ValueError:
		print("\n Введите ЧИСЛО: \n")
		number()

def restart():
	next = input("\nЕще раз ('Да' - д или 'Нет' - н)? \n")
	if next == "Да" or next == "да" or next == "д":
		main()
	elif next == "Нет" or next == "нет" or next == "н":
		exit()
	else:
		print("Да или Нет???")
		restart()

main()