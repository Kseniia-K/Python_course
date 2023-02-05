# print() – выводит данные на экран

# print('Я изучаю Python!')

# между '' и "" кавычками нет разницы, можно использовать оба варианта

# print('Python')
# print("Python")

# несколько аргументов в print() указываются через ,

# print('Скоро я', 'буду программировать', 'на  Python!')
#
# print('1', '2', '4', '8', '16')
#
# print('Какой хороший день!')
# print('Учиться мне не лень.')

# print() – выводит пустую строку

# print('Какой хороший день!')
# print()
# print('Учиться мне не лень!')

# примечание про кавычки

# print('В тексте есть "двойные" кавычки')
# print("В тексте есть 'одинарные' кавычки")
#
# print('Здравствуй, мир!')
#
# print('4', '8', '15', '16', '23', '42')
#
# print('4')
# print('8')
# print('15')
# print('16')
# print('23')
# print('42')
#
# print('*')
# print('**')
# print('***')
# print('****')
# print('*****')
# print('******')
# print('*******')

# input() – считывает введенные с клавиатуры данные

# Вариант 1

# print('Как тебя зовут?')
# name = input()
# print('Привет,', name)

# Вариант 2

# name = input('Как тебя зовут?')
# print('Привет,', name)

# name = input()
# print('Привет,', name)

# footballTeam = input()
# print(footballTeam, '- чемпион!')

# str1 = input()
# str2 = input()
# str3 = input()
#
# print(str1)
# print(str2)
# print(str3)

# str1 = input()
# str2 = input()
# str3 = input()
#
# print(str3)
# print(str2)
# print(str1)

# sep

# print('a', 'b', 'c', sep='*')
# print('d', 'e', 'f', sep='**')

# end

# print('a', 'b', 'c', end='@')
# print('d', 'e', 'f', end='@@')

# print('a', 'b', 'c', sep='*', end='finish')
# print('d', 'e', 'f', sep='**', end='^__^')
# print('g', 'h', 'i', sep='+', end='%')
# print('j', 'k', 'l', sep='-', end='^#')
# print('m', 'n', 'o', sep='/', end='!')

# значения sep и end по умолчанию

# sep = ' ' # пробел
# end = '\n' # перевод строки

# print('a', 'b', 'c', sep='', end='')

# print('a', 'b', 'c', sep='*')
# print('d', 'e', 'f', sep='**', end='')
# print('g', 'h', 'i', sep='+', end='%')
# print('j', 'k', 'l', sep='-', end='\n')
# print('m', 'n', 'o', sep='/', end='!')
# print('p', 'q', 'r', sep='1', end='%')
# print('s', 't', 'u', sep='&', end='\n')
# print('v', 'w', 'x', sep='%')
# print('y', 'z', sep='/', end='!')

# print('I', 'like', 'Python', sep='***')

# separator = input()
# str1 = input()
# str2 = input()
# str3 = input()
# print(str1, str2, str3,sep=separator)

# name = input()
# print('Привет,', name, end='!')

# переменные

# name1 = 'Ксения'
# name2 = name1
# print(name2)

# множественное присваивание

# name, surname = 'Ксения', 'Хохлова'
# print('Имя:',  name, 'Фамилия:', surname)

# name, surname = input(), input()
# print('Имя:',  name, 'Фамилия:', surname)

# name1 = 'Kseniia'
# name2 = 'Kholhlova'
# name1, name2 = name2, name1
#
# print(name1, name2)

# PEP 8

# Избегайте использования пробелов перед открывающей скобкой
# После запятой нужен пробел
# Не отделяйте пробелами знак «равно», когда он употребляется для обозначения значения параметра по умолчанию
# Комментарии должны отделяться хотя бы двумя пробелами от кода, они должны начинаться с символа # и одного пробела

# num1 = 7
# num2 = 10
# num3 = num1 + num2
# print(num3)

# a = 3
# b = 2
# print(a + b)
# print(a - b)
# print(a * b)
# print(a / b)

# num1 = 2 + 3 * 4
# num2 = (2 + 3) * 4
# print(num1)
# print(num2)

# s = '1992'
# year = int(s)

# num1 = int(input())
# num2 = int(input())
# print(num1 + num2)

# num = 17
# s = str(num)

# num1 = -6 # унарный минус
# num2 = 17 - 7 # бинарный минус

# x = int(input())
#
# print(x)
# print(x + 1)
# print(x + 2)

# x = int(input())
# y = int(input())
# z = int(input())
#
# print(x + y + z)

# a = int(input())
# V = a * a * a
# S = 6 * a * a
# print('Объем =', V)
# print('Площадь полной поверхности =', S)

# a = int(input())
# b = int(input())
# f = 3 * ((a + b) ** 3) + 275 * (b ** 2) - 127 * a - 41
# print(f)

# a = int(input())
# print('Следующее за числом', a, 'число:', a + 1)
# print('Для числа', a, 'предыдущее число:', a - 1)

# a1 = int(input())
# a2 = int(input())
# a3 = int(input())
# a4 = int(input())
# print((a1 + a2 + a3 + a4) * 3)

# a = int(input())
# b = int(input())
#
# c = a + b
# d = a - b
# e = a * b
#
# print(a, '+', b, '=', c)
# print(a, '-', b, '=', d)
# print(a, '*', b, '=', e)

# a1 = int(input())
# d = int(input())
# n = int(input())
#
# print(a1 + d * (n - 1))

# x = int(input())
# print(x, '---', 2 * x, '---', 3 * x, '---', 4 * x, '---', 5 * x, sep='')

# print(2 ** 0)
# print(2 ** 1)
# print(2 ** 2)
# print(2 ** 3)
# print(2 ** (-1))

# print(2 ** 2 ** 3) # 2 ** (2 ** 3)

# print(10 // 3)
# print(10 // 4)
# print(10 // 5)
# print(10 // 6)
# print(10 // 12)

# print(10 // 3)
# print(-10 // 3)

# print(10 % 3)
# print(10 % 4)
# print(10 % 5)
# print(10 % 6)
# print(10 % 12)
# print(10 % 20)

# print(23 // 7)
# print(20 // 5)
# print(2 // 5)
# print(123 // 10)
# print(-123 // 10)

# print(23 % 7)
# print(20 % 5)
# print(2 % 5)
# print(123 % 10)

# a = 15 // (16 % 7)
# b = 34 % a * 5 - 29 % 5 * 2
# print(a + b)

# a = 82 // 3 ** 2 % 7
# print(a)

# b1 = int(input())
# q = int(input())
# n = int(input())
#
# print(b1 * q ** (n - 1))

# sm = int(input())
# print(sm // 100)

# n = int(input())
# k = int(input())
#
# print(k // n)
# print(k % n)

# n = int(input())
# print((n + 1) // 2)

# min = int(input())
# print(min, 'мин - это', min // 60, 'час', min - (min // 60) * 60, 'минут.')

# num = 17
# a = num % 10
# b = num // 10
# print(a)
# print(b)

# num = 754
# a = num % 10
# b = (num % 100) // 10
# c = num // 100
# print(a)
# print(b)
# print(c)

# num = int(input())
# last_digit = num % 10
# first_digit = num // 10
# print('Число десятков =', first_digit)
# print('Число единиц =', last_digit)
# print('Сумма цифр =', last_digit + first_digit)
# print('Искомое число =', last_digit * 10 + first_digit)

# num = int(input())
# digit3 = num % 10
# digit2 = (num // 10) % 10
# digit1 = num // 100
# print(digit1, digit2, digit3, sep=',')

# num = int(input())
# digit3 = num % 10
# digit2 = (num // 10) % 10
# digit1 = num // 100
# print('Сумма цифр =', digit1 + digit2 + digit3)
# print('Произведение цифр =', digit1 * digit2 * digit3)

# num = int(input())
# digit3 = num % 10
# digit2 = (num // 10) % 10
# digit1 = num // 100
# print(num)
# print(digit1 * 100 + digit3 * 10 + digit2)
# print(digit2 * 100 + digit1 * 10 + digit3)
# print(digit2 * 100 + digit3 * 10 + digit1)
# print(digit3 * 100 + digit1 * 10 + digit2)
# print(digit3 * 100 + digit2 * 10 + digit1)

# num = int(input())
# digit4 = num % 10
# digit3 = (num % 100) // 10
# digit2 = (num // 100) % 10
# digit1 = num // 1000
#
# print('Цифра в позиции тысяч равна', digit1)
# print('Цифра в позиции сотен равна', digit2)
# print('Цифра в позиции десятков равна', digit3)
# print('Цифра в позиции единиц равна', digit4)

# num = int(input())
# digit5 = num % 10
# digit4 = (num % 100) // 10
# digit3 = (num % 1000) // 100
# digit2 = (num % 10000) // 1000
# digit1 = num // 10000
#
# print(digit1)
# print(digit2)
# print(digit3)
# print(digit4)
# print(digit5)