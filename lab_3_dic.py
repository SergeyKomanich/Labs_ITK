# Task_1

"""
У вхідному рядку записана послідовність чисел через пропуск. Для кожного числа виведіть слово YES (в окремому рядку),
якщо це число раніше зустрічалося в послідовності або NO, якщо не траплялося.
"""

# # Створюємо словник
# numbers_s = {}
#
# # Вводимо рядок чисел через пропуск
# num_input = input('Введіть чісла через пробіл: ')
# # Розділяємо введений рядок на числа
# numbers = num_input.split()
#
# # Перебераємо чісла
# for number in numbers:
#     # Перевіряємо чі є чісло в словніку
#     if number in numbers_s:
#         print('YES')
#     else:
#         print('NO')
#         # Додаємо повторюване чісло до словника, щоб позначіті його "YES"
#         numbers_s[number] = True

# Task_2

"""
 Кожен з деякої множини школярів деякої школи знає кілька мов. Потрібно визначити скільки мов знають усі школярі, 
 і скільки мов знає хоча б один із школярів.
"""
# Створюємо список школярів та мов
school_stud = {
    'Школяр1': {'Іспанська', 'Англійська', 'Українська'},
    'Школяр2': {'Українська', 'Англійська', 'Французька'},
    'Школяр3': {'Іспанська', 'Українська', 'Японська'}
}

# Зберігаємо мову яку знає хоча б один школяр
lang_one_stud = set()
# Зберігаємо мову яку знають усі
lang_all_stud = set()

# Перебереємо школярів та їх мови (.values - відображатиме будь-які зміни)
for stud_lang in school_stud.values():
    # Додаємо мову яку знає хоча б один школяр
    lang_one_stud.update(stud_lang)
    # Якщо мова трапляється вперше то оновлюємо множину
    if not lang_all_stud:
        lang_all_stud.update(stud_lang)
    # Знаходимо спільні мови медодом .intersection_update()
    else:
        lang_all_stud.intersection_update(stud_lang)


print('Кількість мов які знають усі школярі:', len(lang_all_stud))
print('Кількість мов яку знає хоча б один школяр: ', len(lang_one_stud))


# Task_3

"""
Наведено список чисел. Визначте, скільки у ньому зустрічається різних чисел.
"""

numbers = [1, 2, 3, 4, 4, 3, 3, 7, 7, 8, 1, 9, 10]

# Видаляємо повторюванні числа
unique_numbers = set(numbers)

# Знаходимо кількість різних чисел
count_unique_numbers = len(unique_numbers)

print("Кількість різних чисел у списку:", count_unique_numbers)

# Task_4

"""
Даний текст: у першому рядку записано число рядків, далі йдуть самі рядки. 
Визначте, скільки різних слів міститься у цьому тексті.
"""

num_lines = 2      # Кількість рядків
line = """
    Даний текст: у першому рядку записано число рядків, 
    далі йдуть самі рядки. Визначте, скільки різних слів міститься у цьому тексті.
"""

# Зберігаємо унікальні слова
unique_words = set()

for i in range(num_lines):
    # Розділяємо рядок на слова
    words = line.split()
    # Додаємо слова до множини
    unique_words.update(words)
# Знаходимо кількість слів
count_unique_words = len(unique_words)

print('Кількість різних слів у рядках: ', count_unique_words)


# Task_5

"""
Заповніть один кортеж десятьма цілими числами від 0 до 5 включно. 
Також заповніть другий кортеж числами від -5 до 0. 
Щоб заповнити кортеж числами, напишіть одну функцію. 
Об'єднайте два кортежі за допомогою оператора +, створивши цим третій кортеж. 
За допомогою методу кортежу count() визначте у ньому кількість нулів. 
Виведіть на екран третій кортеж та кількість нулів у ньому.
"""

# Створюємо функцію щоб заповнити кортежі числами
def num_tuple(start, end):
    return tuple(range(start, end + 1))

# Заповнюємо перший кортеж
tuple_1 = num_tuple(0, 5)

# Другий кортеж
tuple_2 = num_tuple(-5, 0)

# Об'єднуємо кортежі
tuple_3 = tuple_1 + tuple_2

# методом .count() знаходимо кількість 0 у кортежі 3
zero_count = tuple_3.count(0)

print('Третій кортеж: ', tuple_3)
print('Кількість нулів у ньому: ', zero_count)
print(tuple_1)
print(tuple_2)


# Task_6

"""
Напишіть програму для злиття кількох словників на один.
"""
dict_1 = {'a': 1, 'b': 2, 'c': 3}
dict_2 = {'d': 4, 'e': 5, 'f': 6}
dict_3 = {'g': 7, 'h': 8, 'i': 9}

# Збираємо словники
list_dict = [dict_1, dict_2, dict_3]

# Функцією dict() зливаємо словники
dict_merged = dict()
for i in list_dict:
    dict_merged.update(i)

print("Об'єднаний словник:", dict_merged)

# Task_7
"""
Дано два списки чисел. Знайдіть усі числа, 
які входять як до першого, так і до другого списку і виведіть їх у порядку зростання.
"""

list1 = [3, 2, 5, 7, 10]
list2 = [2, 5, 10, 8, 9]

# Перетворюємо списки у множини
set1 = set(list1)
set2 = set(list2)

# Знаходимо спільні числа за допомогою операції перетину множин (.intersection(), повертає значення які містяться у обох множинах
sort_numbers = sorted(list(set1.intersection(set2)))

print("Спільні числа у порядку зростання:", sort_numbers)









