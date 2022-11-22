from random import randint

A = 5
a = [randint(-10, 10) for i in range(A)]
b = [randint(-10, 10) for i in range(A)]

print(f"Список a: {a}")
print(f"Список b: {b}")

print(f"Список с элементами обоих списков: {a}{b}")

i = []
for element in a:
    i.append(element)
for element in b:
    if element not in i:
        i.append(element)
print(f"Список c элементами обоих списков без повторений: {i}")

i = []
for elementa in a:
    for elementb in b:
        if elementa == elementb:
            i.append(elementa)
print(f"Список c общими элементами: {i}")

i = []
for element in a:
    if element not in b:
        i.append(element)
for element in b:
    if element not in a and element not in i:
        i.append(element)
print(f"Список c уникальными элементами обоих списков: {i}")

i = [min(a), max(a), min(b), max(b)]
print(f"Список c максимумом и минимумом списков: {i}")
