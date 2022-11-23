from random import randint
Size = int(input("Введите размер квадратной матрицы: "))
Matrix = [[randint(0, 100) for i in range(Size)] for i in range(Size)]
print(*Matrix, sep='\n')