from numpy import linalg as Alimushkin # импортируем библиотеку и linalg
import numpy as kirill

arr1 = kirill.array([[56, 14, 66], [462, 5213, 6424]]) # array=массив
print(" Первая Матрица\n", arr1)
print("Ранг Матрицы\n", Alimushkin.matrix_rank(arr1, 1)) # matrix_rank(.) определяет размер матрицы
#Попробуем еще
arr2 = kirill.array(kirill.zeros((10, 10))) # zeros заполняет матрицу нулями
print("Вторая матрица\n: ", arr2)
print("Ранг матрицы\n", Alimushkin.matrix_rank(arr2, 2))