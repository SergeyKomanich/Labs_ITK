import math

# Task_1

"""
Вивести на екран таблицю
x | 1 | 2 | 3 | 4 | 5
---+---+---+---+---+---
y | 3 | 1 | 5 | 4 | 2
"""


print('x', 1, 2, 3, 4, 5, sep=' | ')
print('---+---+---+---+---+---')
print('y', 3, 1, 5, 4, 2, sep=' | ')

#Task_2

# дано натуральне число. Знайти суму цифр цьго числа

x = int (input('Введіть трьохзначне число '))
first_num = x // 100
second_num = x // 10 % 10
third_num = x % 10
suma = first_num + second_num + third_num

print('Сума цифр числа %d = %d' % (x, suma))

# Task_3

# Обчисліть гіпотенузу з прямокутного трикутника за катетами a та b

a = float(input('Введіть значення катета a: '))
b = float(input('Введіть значення катета b :'))
gipotenuza = math.sqrt(a**2 + b**2)

print('Гіпотенуза = ', round(gipotenuza, 3))

# Task_4

#Наближено визначити значення числа π, використовуючи ланцюговий дріб

pi = 3 + 1 / (7 + 1 / (15 + 1 / (1 + 1 / 292)))

print(pi)

# Task_5

#Обчислити значення многочлена для введеного з клавіатури комплексного числа 𝑧:
#a)𝑓(𝑧)=4𝑧4 +3𝑧3 +2𝑧2 +𝑧+1;

z = complex(input('Введіть комплексне число z у форматі "a+bj": '))
f = 4 * z**4 + 3 * z**3 + 2 * z**2 + z + 1

print(f)

# b)𝑓(𝑧)=𝑧4 +2𝑧2 +1;

z_2 = complex(input('Введіть комплексне число z у форматі "a+bj": '))
f_2 = z_2**4 + 2 * z_2**2 + 1

print(f_2)


# Task_6

"""
Скласти програми для розв'язання рівнянь:
a) 4.2343𝑥 + 𝑏 = 𝑐; b) (5.23𝑥 + 𝑏)(𝑑 − 2.4𝑦) = 0; c) 𝑎𝑥 + 𝑏 = 𝑐𝑥 + 𝑑, 𝑎 − 𝑐 ≠ 0,
де коефіцієнти 𝑎, 𝑏, 𝑐, 𝑑 – вводяться з клавіатури.
"""


# a) 4.2343𝑥 + 𝑏 = 𝑐

b = int(input('Введіть значення b: '))
c = int(input('Введіть значення c: '))

x = (c - b) / 4.2343

print("x =", x)

# b) (5.23𝑥 + 𝑏)(𝑑 − 2.4𝑦) = 0

b = float(input('Введіть значення b: '))
d = float(input('Введіть значення d: '))

x = -b / 5.23
y = d / 2.4

print('Значення х: ', x)
print('значення у: ', y)

# c) 𝑎𝑥 + 𝑏 = 𝑐𝑥 + 𝑑, 𝑎 − 𝑐 ≠ 0

a = float(input('Введіть значення a: '))
b = float(input('Введіть значення b: '))
c = float(input('Введіть значення c: '))
d = float(input('Введіть значення d: '))

# Переносимо всі члени, що містять х, на одну сторону рівності

# a * x - c * x = d - b
# (a - c) * x = d - b

x = (d - b) / (a - c)

print('Значення х: ', x)

# Task_7

# Дано натуральне чотиризначне число. Знайти суму цифр цього числа

num = int(input('Введіть чотиризначне число: '))

num_1 = num // 1000
num_2 = (num // 100) % 10
num_3 = (num // 10) % 10
num_4 = num % 10

sum_digits = num_1 + num_2 + num_3 + num_4

print('Сума цифр числа: ', sum_digits)


# Task_8

# Обчислити катет а c прямокутного трикутника за гіпотенузою с та катетом b.

c = float(input('Введіть гіпотенузу с: '))
b = float(input('Введіть гіпотенузу b: '))

a = math.sqrt(c**2 - b**2)

print('Катет a = ', a)

# Task_9

# Наближено визначити період обертання Землі навколо Сонця, використовуючи ланцюговий дріб
# T = 365 + 1/(4 + 1/(7 + 1/(1 + 1/3)))

t = 365 + 1 / (4 + 1 / (7 + 1 / (1 + 1 / 3)))

print('Період обертання Землі навколо Сонця =', t)

# Task_10

"""
Обчислити значення многочлена для введеного з клавіатури комплексного числа 𝑧:
𝑓(𝑧) = 15𝑧41 + 31𝑧31 + 2𝑧25 + 𝑧-1 + 1;
𝑓(𝑧) = 256𝑧41 + 22𝑧28 + 51;
"""

z = complex(input('Введіть комплексне число у форматі "a+bj": '))

f_z = 15 * z**41 + 31 * z**31 + 2 * z**25 + z**(-1) + 1

print('Значення многочлена f(z) для комплексного числа z:', f_z)


# 𝑓(𝑧) = 256𝑧41 + 22𝑧28 + 51;

z_2 = complex(input('Введіть комплексне число у форматі "a+bj": '))

f_z_2 = 256 * z_2**41 + 22 * z_2**28 + 51

print('Значення многочлена f(z) для комплексного числа z:', f_z_2)













