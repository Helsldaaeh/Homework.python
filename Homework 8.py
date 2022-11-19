Menu = input("Выберите фигуру которую хотите получить:\n\
А - Это тругольник построенный вершиной в верхний правый угол, основание - диагональ диагональ квадрата, всё это находится в квадрате;\n\
Б - То же что и а только вершина в нижнеем левом углу, всё это находится в квадрате;\n\
В - Равнобедренный треугольник сверху до центра квадрата, всё это находится в квадрате;\n\
Г - То же что и в только снизу, всё это находится в квадрате;\n\
Д - Это г + в, всё это находится в квадрате;\n\
Е - Это то же самое что и д только перенесено на другие паралельные стороны, всё это находится в квадрате;\n\
Ж - Равнобедренный треугольник с левой части, до центра, всё это находится в квадрате;\n\
З - Это то же что и \'ж\', только справа, всё это находится в квадрате;\n\
И - Это тругольник построенный вершиной в верхний левый угол, основание - диагональ квадрата, всё это находится в квадрате; \n\
К - То же что и \'и\', только вершина в правом нижнем углу, всё это находится в квадрате.\n\
")# Задание 1 убил 2 часа всё равно не понятно

Count1 = 30 
Count2 = 0
Count3 = 15
Count4 = 0
Count5 = 15


if Menu == "И":
    while Count2 != 30:
        print(Count1 * "*", Count2 * " ")
        Count1 -= 1
        Count2 += 1
if Menu == "Б":
    while Count2 != 30:
        print(Count2 * "*", Count1 * " ")
        Count1 -= 1
        Count2 += 1
if Menu == "А":
    while Count2 != 30:
        print(Count2 * " ", Count1 * "*")
        Count1 -= 1
        Count2 += 1
if Menu == "К":
    while Count2 != 30:
        print(Count1 * " ", Count2 * "*")
        Count1 -= 1
        Count2 += 1
if Menu == "Г":
    while Count2 != 15:
        print(Count3 * " ", Count2 * "*", Count2 * "*", Count3 * " ")
        Count3 -= 1
        Count2 += 1
if Menu == "В":
    while Count2 != 15:
        print(Count2 * " ", Count3 * "*", Count3 * "*", Count2 * " ")
        Count3 -= 1
        Count2 += 1
if Menu == "Д":
    while Count4 != 15:
        print(Count4 * " ", Count5 * "*", Count5 * "*", Count4 * " ")
        Count5 -= 1
        Count4 += 1
    while Count2 != 15:
        print(Count3 * " ", Count2 * "*", Count2 * "*", Count3 * " ")
        Count3 -= 1
        Count2 += 1
if Menu == "Ж":
    while Count2 != 15:
        print(Count2 * "*", Count3 * " ")
        Count3 -= 1
        Count2 += 1
    while Count4 != 15:
        print(Count5 * "*", Count4 * " ")
        Count5 -= 1
        Count4 += 1
if Menu == "З":
    while Count2 != 15:
        print(Count3 * " ", Count2 * "*")
        Count3 -= 1
        Count2 += 1
    while Count4 != 15:
        print(Count4 * " ", Count5 * "*")
        Count5 -= 1
        Count4 += 1
if Menu == "Е":
    while Count2 != 15:
        print(Count2 * "*", Count3 * " ", Count3 * " ", Count2 * "*")
        Count3 -= 1
        Count2 += 1
    while Count4 != 15:
        print(Count5 * "*", Count4 * " ", Count4 * " ", Count5 * "*")
        Count5 -= 1
        Count4 += 1

from random import randint # Задание 2
listA = [randint(-100,100) for i in range(10)]
print("Чётные числа: ",sum(i % 2 == 0 for i in listA ))
print("Нечётные числа: ",sum(i % 2 != 1 for i in listA ))
print("Отрицательные числа: ",sum(i < 0 for i in listA ))
print("Положительные числа: ",sum(i > 0 for i in listA ))