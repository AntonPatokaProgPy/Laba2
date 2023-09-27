x = []

print("Заполняем первую матрицу 3x3 через пробел по 3 элемента")
for i in range(3):
    x.append(list(map(int, input().split()))) #Заполняем матрицу 3x3
y = []
print("Заполняем вторую матрицу 3x3 через пробел по 3 элемента")
for i in range(3):
    y.append(list(map(int, input().split()))) #Заполняем матрицу 3x3

pm = [[0, 0, 0],
      [0, 0, 0],   #Создаем пустую матрицу для для хранения результата умножения
      [0, 0, 0]]

for a in range(len(x)):
    for b in range(len(y[0])):  # Используем вложеный цикл для матриц Х и У
        for c in range(len(y)):
            pm[a][b] += x[a][c] * y[b][c]  # Сохранение результата умножения в пустой матрице


for res in pm:
    print(*res)


