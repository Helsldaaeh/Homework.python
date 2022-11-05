A = int(input("Введите номер дня недели: "))#Задание 1
if A == 1:
    print("Понедельник")
elif A == 2:
    print("Вторник")
elif A == 3:
    print("Среда")
elif A == 4:
    print("Четверг")
elif A == 5:
    print("Пятница")
elif A == 6:
    print("Суббота")
elif A == 7:
    print("Воскресенье")
else:
    print("Номер больше 7")
    print()
B = int(input("Введите номер месяца: "))#Задание 2
if B == 1:
    print("Январь")
elif B == 2:
    print("Февраль")
elif B == 3:
    print("Март")
elif B == 4:
    print("Апрель")
elif B == 5:
    print("Май")
elif B == 6:
    print("Июнь")
elif B == 7:
    print("Июль")
elif B == 8:
    print("Август")
elif B == 9:
    print("Сентябрь")
elif B == 10:
    print("Октябрь")
elif B == 11:
    print("Ноябрь")
elif B == 12:
    print("Декабрь")
else:
    print("Не верный номер")
    print()
C = int(input("Введите число: "))#Задание 3
if C > 0:
    print("Число положительно")
elif C < 0:
    print("Число негативное")
else:
    print("Число равняется 0")
    print()
a = int(input("Введите число: "))#Задание 4
b = int(input("Введите число: "))
if a == b:
    print("Числа равны")
elif a > b:
    print(b,a)
else:
    print(a,b)
    print()
z = int(input("введите число: "))#Задание 5
x = int(input("Введите число: "))
c = int(input("Введите число: "))
Q = int(input("Введите процесс 2 - Суммирование или 1 - Произведение)"))
if Q == 1:
    print(z*x*c)
elif Q == 2:
    print(z+x+c)
else:
    print("Неправильно введённый Q")
    print()
Z = int(input("Введите число: "))#Задание 6
X = int(input("Введите число: "))
C = int(input("Введите число: "))
q = int(input("Введите либо 1 - Максимум из трёх чисел,\n либо 2 - Минимум из трёх,\n либо 3 - Среднее арифметическое"))
e = z+x+c
if q == 1:
    print(max(z,x,c))
elif q == 2:
    print(min(z,x,c))
elif q == 3:
    print(e/3)
    print()
I = int(input("Введите количество метров: "))#Задание 7
i = int(input("Во что переводить 1(Мили), 2(Дюймы), 3(Ярды)"))
if i == 1:
    print(I*1609,"Миль")
elif i == 2:
    print(I*0.0254,"Дюймы")
elif i == 3:
    print(I* 0.9144,"Ярды")
else:
    print("Неверно указано i")