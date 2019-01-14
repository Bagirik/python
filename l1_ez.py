__author__ = 'Куликова Таисия Сергеевна'
# Lesson, easy
# Задача-1
n = input()
for i in n:
    print(i)

# Задача-2
a = input(' Введите a: ')
b = input(' Введите b: ')
c = ''
c = a
a = b
b = c
print(a, " Это было b")
print(b, " Это было а")

# Задача-3
age = int(input('Укажите Ваш возраст '))
if age >= 18:
    print('Доступ разрешен')
else:
    print('Извините, пользование данным ресурсом только с 18 лет')
