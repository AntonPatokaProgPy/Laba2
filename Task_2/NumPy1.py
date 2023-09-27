#ПЕРВОЕ ЗАДАНИЕ
import numpy as kirill  # Берем библиотеку numpy

Shiza = kirill.arange(9).reshape((3, 3)) #arange(9) делает последовательность цифр 0-8 с шагом в 1 \\\reshape (3.3) делает маьрицу 3x3
print("Класическая матрица")
print(Shiza)

antiShiza = kirill.transpose(Shiza) # np.transpose(в моем случае kirill.transpose) транспортирует матрицу
print("Транспортированная Матрица")
print(antiShiza)

# Покажем,что это работает в любом случае

Shza = kirill.arange(100).reshape((10, 10)) # меняем arange и reshape
print("Класическая матрица 2.0")
print(Shza)

antiShza = kirill.transpose(Shza)
print("Транспортированная Матрица 2.0")
print(antiShza)