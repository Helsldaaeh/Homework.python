Num1 = int(input("Введите первое число: "))# Задание 1
Num2 = int(input("Введите второе число: "))
A = str(input("Введите действие: "))
list = ["+", "-", "*", "/"]

if A == "+":
    print( Num1, "+", Num2, "=", Num1 + Num2 )
elif A == "-":
    print( Num1, "-", Num2, "=", Num1 - Num2 )
elif A == "*":
    print( Num1, "*", Num2, "=", Num1 * Num2 )
elif A == "/":
    print( Num1, "/", Num2, "=", Num1 / Num2 )
if A not in list:
    print("Такой команды нет в списке")


from random import randrange#ПСДЖЖЖ задание 2

size = 6
list = [randrange(-100,100) for i in range(size)]
print("Максимальное число: ", max(list))
print("Минимальное число: ", min(list) )
i = 0

print("Сумма положительных чисел: ", sum(i > 0 for i in list))

print("Сумма отрицательных чисел: ", sum(i < 0 for i in list))

print("Сумма нулей: ", sum(i == 0 for i in list))