# from colorama import init
# from colorama import Fore, Back, Stylefrom colorama

def add(x, y):
	return str(x + y)

def main():
	# print(Fore.BLACK) 
	# print(Back.CYAN)
	operation()
	# print(Back.RED)
	a = float(input("Первое число: "))
	b = float(input("Второе число: "))
	# print(Back.YELLOW)

	if what == "+":
		print("Результат:" + add(a, b))

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
		return float(input(prompt))
	except ValueError:
		print("\n Введите число \n")
		number()

def restart():
	next = input("\nЕще раз (Да или Нет)? \n")
	if next == "Да" or next == "да" or next == "д":
		main()
	elif next == "Нет" or next == "нет" or next == "н":
		exit()
	else:
		print("Да или Нет???")
		restart()

main()