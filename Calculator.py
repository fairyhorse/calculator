# from colorama import init
# from colorama import Fore, Back, Style

# print(Fore.BLACK)

# print(Back.CYAN)

what = input("Выберите знак (+, -, *, /): \n")

# print(Back.RED)

a = float(input("Введите первое число: \n"))
b = float(input("Введите второе число: \n"))

# print(Back.YELLOW)

if what == "+":
    c = a + b
    
    print("Результат:" + str(c))    
    
elif what == "-":
    c = a - b
    
    print("Результат:" + str(c))   
    
elif what == "*":
    c = a * b
    
    print("Результат:" + str(c))
    
elif what == "/":
    c = a / b
    
    print("Результат:" + str(c))
    
else:
    print("Error")


input()