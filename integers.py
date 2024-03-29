"==========Числа=========="
# integers(int) - целые числа

num = 5
print(type(num)) # <class 'int'>

num1 = '10'
num1 = int(num1)

print(type(num1)) 
# <class 'str'> if ->
# num1 = '10'
# print(type(num1))

# float - вещественные числа (с плавающей точкой, десятичные)

a = 10.5

print(type(a)) # <class 'float'>

b = float(23)
print(b) # 23.0

c = float('45.9')
print(type(c)) # <class 'float'>

print(0.1+0.1+0.1+0.1+0.1+0.1+0.1+0.1+0.1+0.1)

# decimal - точное вещественное число
# чтобы использовать decimal, нужно его импортировать

from decimal import Decimal

a = Decimal('0.1')

print(a+a+a+a+a+a+a+a+a+a+a)

"==========Операции над числами==========="

5 + 7 # сложение
10 - 5 # вычитание
2 * 5 # умножение
100 / 10 # деление
15 // 3 # деление 
5 % 2 # остаток от деления 1
2**3 # возведение в степень 2*2*2
25**0.5 # нахождение кв. корня числа

# модуль числа - это когда из отрицательного числа получаем положительное |-5| = 5
print(abs(-5)) # 5
print(abs(10)) # 10
print(abs(-0.1)) # 0.1

# round - округление числа
print(round(5.6)) # Округление в большую сторону, если число больше x.6 | 5.6 - 6
print(round(5.5)) # 5.5 будет 6 | x.5 - округление в большую сторону
print(round(5.4)) # 5.4 будет 5 | если x.4 и меньше, округление в меньшую сторону

print(round(10/3, 1)) # "1" убирает числа после запятой
print(round(10.0007852, 4)) # 10.0008
print(round(10.0476, 3)) # 10.048

# sqrt - функция для нахождения кв. корня числа
# его нужно импортировать
from math import sqrt

print(sqrt(25)) # 5.0
print(sqrt(36)) # 6.0
print(sqrt(34)) # 5.830951894845301

# pow
# 1) возводит в степень
# 2) деление с остатком
print(pow(2, 3)) # 8 | 2**3 = 8
print(pow(2, 3, 4)) # 0 | 2**3%4 = 0

# divmod - функция, которая возвращает два числа, где первое, целая часть от деления, второе - остаток от деления -->
# -> Делит и показывает остаток | деление округляет
print(divmod(5, 2)) # (2, 1) | 5//2 5%2
print(divmod(17, 3)) # (5, 2) | 17//3 17%3
print(divmod(10, 5)) # (2, 0) | 10//5 10%5
print(divmod(10, 3)) # (3, 1) | 10//3 10%3