age = int(input("Введите свой возраст: "))
height = int(input("Введите свой рост: "))

if height>180:
    print("Ура")

print(height > 180)


a = int(input("введите число: "))
if a % 2:
    print("Чётное число")
else:
    print("Нечётное число")

b=int(input("Введите число: ")) 
if b % 7:
    print("Число кратно 7")
else:
    print("Число не кратно 7")

op = int(input("Введите оператор (+, -, *, /): "))

n1 = float(input("Введите число 1: "))
n2 = float(input("Введите число 2: "))
if op == "+":
    print(n1, op, n2, "=",n1 + n2)
elif op == "-":
    print(n1, op, n2, "=",n1 - n2)
elif op == "*":
    print(n1, op, n2, "=",n1 * n2)
elif op == "/":
    print(n1, op, n2, "=",n1 / n2)
else:
    print("Такого оператора не существует")

c = int(input("Введите двухзначное число: "))
if 9< c <100:
    print(c // 10)
    print(c % 10)
else:
    print("число не двухзначное")


v = 0

while v<10:
    v+=1
    print(v)

print("Цикл завершён")

tmp_d=d = int(input("введите номер билета: ")) 
#инициализация переменных
last_n=first_n=new_d = i = 0
#пока d
while d !=0:
    #берем последнюю цифру числа
    n = d % 10
    #берём последнюю цифру из числа
    d //=10
    #удаляем последнюю цифру из числа
    if i ==0:
        last_n = d
    elif i ==5:
        first_n = d
#увеличиваем счётчик
    i += 1
new_n = last_n *10000 + tmp_d % 10000
#593820 + 7 = 593827
new_d=new_d//10 * 10 + first_n

print(new_d)