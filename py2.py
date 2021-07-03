from colorama import init
from colorama import Fore, Back, Style
init()
print ( Back.CYAN )
what = input ("Что делаем: + - * / ?")

a = float (input ("Введите первое число: ") )
b = float (input ("Введите второе число: ") )
if what == "+":
    print (a + b)
elif what == "-":
    print (a - b)
elif what == "*":
    print (a * b)
elif what == "/":
    print (a / b)
else: print ("Данна операция не поддерживается")
