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
# Rомментарии должны отделяться хотя бы двумя пробелами от кода, они должны начинаться с символа # и одного пробела

