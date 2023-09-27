import timeit
import numpy as np
import numpy


# Транспонирование матрицы (т.е меняем строки местами с столбцами
def trans(m_x):
    m_x[1][0], m_x[0][1] = m_x[0][1], m_x[1][0]
    m_x[2][0], m_x[0][2] = m_x[0][2], m_x[2][0]
    m_x[2][1], m_x[1][2] = m_x[1][2], m_x[2][1]
    return m_x


# Вычисляем опеределитель методом звезды
def delta_mx(m_x):
    return (m_x[0][0] * m_x[1][1] * m_x[2][2] + m_x[0][1] * m_x[1][2] * m_x[2][0] + m_x[1][0] * m_x[2][1] * m_x[0][2]
            - m_x[0][2] * m_x[1][1] * m_x[2][0] - m_x[0][1] * m_x[1][0] * m_x[2][2] - m_x[0][0] * m_x[1][2] *
            m_x[2][1])


# Вычисляем минор
def minr_3x3(a):
    minor = []
    for i in range(3):
        for j in range(3):
            if i == 0 and j == 0:
                minor.append((-1) ** (j + 1 + i + 1) * (a[1][1] * a[2][2] - a[1][2] * a[2][1]))
            if i == 0 and j == 1:
                minor.append((-1) ** (j + 1 + i + 1) * (a[1][0] * a[2][2] - a[1][2] * a[2][0]))
            if i == 0 and j == 2:
                minor.append((-1) ** (j + 1 + i + 1) * (a[1][0] * a[2][1] - a[1][2] * a[2][0]))
            if i == 1 and j == 0:
                minor.append((-1) ** (j + 1 + i + 1) * (a[0][1] * a[2][2] - a[0][2] * a[2][1]))
            if i == 1 and j == 1:
                minor.append((-1) ** (j + 1 + i + 1) * (a[0][0] * a[2][2] - a[0][2] * a[2][0]))
            if i == 1 and j == 2:
                minor.append((-1) ** (j + 1 + i + 1) * (a[0][0] * a[2][1] - a[0][1] * a[2][0]))
            if i == 2 and j == 0:
                minor.append((-1) ** (j + 1 + i + 1) * (a[0][1] * a[1][2] - a[0][2] * a[1][1]))
            if i == 2 and j == 1:
                minor.append((-1) ** (j + 1 + i + 1) * (a[0][0] * a[1][2] - a[0][2] * a[1][0]))
            if i == 2 and j == 2:
                minor.append((-1) ** (j + 1 + i + 1) * (a[0][0] * a[1][1] - a[0][1] * a[1][0]))
    return minor


def Reverse(a):
    connect = minr_3x3(trans(a))
    c = 0
    for i in range(len(minr_3x3(trans(a)))):
        print(f'{connect[i] * (1 / delta_mx(a)):.2}', end=' ')
        c += 1
        if c == 3:
            print('')
            c = 0

print("Заполните матрицу 3x3 через пробел по 3 элемента: ")
a = [list(map(int, input().split())) for _ in range(3)]  # Заполение матрицы через пробел
if delta_mx(a) == 0:
    print("Нельзя вычислить обратную матрицу")
else:
    Reverse(a)

print(timeit.timeit('Reverse(a)', number=1, globals=globals()))
print('↑')
print("Время работы самописной функции Reverse ")
print("Время работы функции из NumPy")
print("↓")
print(timeit.timeit('np.linalg.inv(a)', number=1, globals=globals()))
