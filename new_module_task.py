# 6. Словники. (Middle: 1 point)
#     Створити алгоритм гри "Містечка". Тобто правила такі:
#     Є словник зі столицями країн. (10 столиць країн на твій вибір)
#     Користувач "нескінченно" вводить назву міст і програма на основі словника видає відповідь так
#     це столиця такої країни чи ні на жаль це не столиця якщо такої столиці у 10 країн зі словника немає.
#     або введіть слово стоп, яке закінчить цикл.
#     Користувач введе Токіо - Програма поверне Японія (це за умов що ця країна зазначена в словнику)


# 7. Перетворення словників (Middle: 1 point)
# 	Створити на основі англо-латинського словника латино-англійський словник.
# 	Тобто на основі прикладу нижче створити алгоритм, який перетворить словник мовою python)
# 	Вхідні дані (словник приклад):
# 		{ "apple" : ['malum', 'omum', 'popula'],
# 		'fruit' : ['baca', 'bacca', 'popum'],
# 		'punishment' : ['malum', 'multa'],
# 		'dog' : 'canina'}
# На виході отримаємо:
# 	{'malum': ['apple', 'punishment'],
# 	'omum': 'apple',
# 	'popula': 'apple',
# 	'baca': 'fruit',
# 	'bacca': 'fruit',
# 	'popum': 'fruit',
# 	'multa': 'punishment',
# 	'canina': 'dog'}
# *Відповідь робити не руками а алгоритмом! Тобто вхідний словник перетворити алгоритмом на словник латино-англійських слів
# 	**словник приклад - це означає, що даний словник є зразковим, а ваш алгоритм буде протестований на більшому словнику,
# 	  тобто немає сенсу писати підігнаний алгоритм, а необхідно написати універсальний алгоритм.

# 8. Рядкові паттерни (Middle*: 1.5 point)
# 	Створіть функцію, яка перевіряє, чи даний рядок складається з шаблону підрядка,
# 	який повторюється кілька разів на протязі вього рядка, то повернути True або False якщо такого шаблону не існує.
# приклади:
# 	"a" ➞ False
# 	"ababab" ➞ True
# 	"aabb" ➞ False
# 	"abcabcabcabc" ➞ True
# 	"abcabccba" ➞ False
# 	"aaaa" ➞ True

# 9. Дужки та рядки (Middle**: 1.7 point)
# 	Cтворити функцію, яка приймає рядок дужок і повертає допустимий порядок фігурних дужок чи ні.
# 	Всі вхідні рядки будуть непустими і будуть складатися тільки з дужок: () [] {}.
# 	Що вважається дійсним? Рядок фігурних дужок вважається дійсним, якщо всі дужки складаються в правильну послідовність,
# 	тобто є відкриті та закриті дужки одного виду на оденому рівні.
# 	Приклади:
# 	"(){}[]" ➞ True
# 	"([{}])"  ➞ True
# 	"(}"    ➞ False
# 	"[(])"  ➞ False
# 	"[({})](]" ➞ False

# 10. Файли та рядки (Hard: 2.5 point)
# 	Обробити файл (файл у додатку до завдання) та знайти найдовше слово в даному фа йлі(file_1.txt).
# 	Далі Дoзаписати це слово назад у файл, але тільки всі літери повинні бути КАПСОМ (записати теж слово,
# 	але тільки великими літерами).
words = []
with open('new_file.txt') as fl:
    for el in fl:
        words.append([(i) for i in el.split()])

print(words)