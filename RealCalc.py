import math
from colorama import init
from colorama import Fore, Back, Style

def main():
	global a, b, c, res
	print(Fore.BLACK) 
	print(Back.RED)
	a = number()
	print(Back.CYAN)	
	operation()
	print(Back.RED)
	b = number()
	print(Back.YELLOW)
	res = result(a, b)
	print(str(res))	
	next()
	restart()

def operation():
	global what
	accepted = ['+', '-', '*', '/', '^']
	what = input()	
	if what not in accepted:
		operation()

def number():
	while True:
		try:
			return float(input())
		except ValueError:
			print("\nEnter a NUMBER \n")

#def result():
#	try:
#		enter = input()
#		if enter == "":
#			pass
#		else:
#			result()
#	except TypeError:
#		result()

def next():
	next = input("Continue? (Yes or no)\n")	
	if next == "Yes" or next == "yes":
		result2()
	else:
		restart()

def result(x, y):
	if what == "+":
		return (x + y)
	elif what == "-":
		return (x - y)
	elif what == "*":
		return (x * y)
	elif what == "/":
		try:
			return (x / y)
		except ZeroDivisionError:
			print("CANNOT DIVIDE BY ZERO!")
			restart()			
	elif what == "^":
		try:
			return(pow(x, y))
		except OverflowError:
			print("Result is too large!")
			restart()

def result2():
	global res, res2
	print(Back.CYAN)
	operation()
	print(Back.RED)
	c = number()
	print(Back.YELLOW)	
	res2 = result(res, c)
	print(str(res2))
	res = res2
	next()

def restart():
	restart = input("\nAgain? (Yes or No) \n")
	if restart == "Yes" or restart == "yes":
		main()
	elif restart == "No" or restart == "no":
		exit()
	else:
		print("Yes or No???")
		restart()
			
main()