"===============Переменные==============="

# Переменная - это ссылка на ячейки памяти, где хранятся какие-то данные

[[10],['xep'],[]]

num1 = 10
num2 = 45

print(num1)
print(num1+num2)

"===============Правила наименования переменных==============="

a = 5 # | по назначению
# 1num = 5 | нельзя начинать название с чисел
# num-li1 = 5 | нельзя использовать символы кроме " _ "
# hello world = 6 | нельзя использовать пробелы в названии
# print = 10 нельзя называть названиями переменных

hello_world = 5 # snake case

helloWorld = 6 # camel case

"===============Ввод и вывод данных==============="

# print - функция вывода данных  в терминал
# input - функция ввода данных в терминале

number = input('Ввеите любое число: ')
print('Введённое вами число - ', number)

"===============Типы данных==============="
# Типы данныъ делятся на 2 вида: изменяемые, неизменяемые
# Изменяемые: list(список), dict(словарь), set(множества)
# Неизменяемые: int, float, complex, str, tuple, bool, None


# Изменяемые
list_ = [1,2,3,4]
dict_ = {'a':1, 'b':2}
set_ = {1,2,3,4}

# Неизменяемые
int_ = 10
float_ = 0.5
str_ = "Hello world"
tuple_ = (1,2,3,4)
bool_1 = True
bool_0 = False
none_ = None

print('изменяемые типы', list_, dict_, set_)
print('неизменяемые типы', int_, float_, str_, tuple_, bool_1, bool_0, none_)