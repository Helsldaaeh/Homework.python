A = int(input("Введите сторону квадрата: "))
B = str(input("Введите символ для заполнения: "))

for i in range(A):
    i = A
    print(B*i)


a = int(input("Введите высоту прямоугольника: "))
b = int(input("Введите длину прямоугольника: "))
c = str(input("Введите символ для заполнения: "))

for t in range(a):
    t = b
    print(t*c)


C = int(input("Введите высоту: "))
E = int(input("Введите длину: "))
P = str(input("Введите символ для границ: "))
F = " "

print(E*P)

for f in range(C - 2):
    if E > 2:
        f = E - 4
        print(1*P,F*f,1*P)
    else:
        for d in range(C - 2):
            d = E
            print(d)

print(E*P)


