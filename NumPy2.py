import numpy as kirill  #Берем библиотеку numpy

arr1 = kirill.array([[2, 4], [6, 8]]) # array=массив
print("Первая Матрица")
print(arr1)
print("Размер Первой Матрицы", arr1.shape) # shape= Размер матрицы пример: 2x2,3x5 и тд

arr2 = kirill.array([[1, 3], [5, 7]]) # аналогично
print("Вторая матрица ")
print(arr2)
print("Размер Второй Матрицы", arr2.shape) # точно также

mama1top = kirill.matmul(arr1, arr2) #matmul=умножение
print("Результат Произведения Матриц ")
print(mama1top)
print("Размер Произведения Матриц", mama1top.shape)



arr3 = kirill.array([[2, 4,6], [6, 8,7],[7,9,4]])
print("Первая Матрица")
print(arr3)
print("Размер Первой Матрицы", arr3.shape)

arr4 = kirill.array([[1, 3,6], [5, 7,8],[6,8,2]])
print("Вторая матрица ")
print(arr4)
print("Размер Второй Матрицы", arr4.shape)

mama2top = kirill.matmul(arr3, arr4)
print("Результат Произведения Матриц ")
print(mama2top)
print("Размер Произведения Матриц", mama2top.shape)