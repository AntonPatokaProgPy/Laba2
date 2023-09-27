# Проверим ее совместимость с интерактивом
import numpy as kirill
print('Пример ввода Данных \n ''a b c \n d e f \n r v o')# визуальный кайф
print('Введите a')
a= input()
print('Введите b')
b= input()
print('Введите c')
c= input()
print('Введите d')
d= input()
print('Введите e')
e= input()
print('Введите f')
f= input()
print('Введите r')
r= input()
print('Введите v')
v= input()
print('Введите o')
o= input()
Shza=[[a,b,c],# моя красотень
    [d,e,f],
    [r,v,e]]

antiShza = kirill.transpose(Shza)
print("Транспортированная Матрица 2.0")
print(antiShza)