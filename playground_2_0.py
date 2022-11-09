# 1. Сворити список мінімум з 10 й елементів(тип данних для простоти int або float)
# 	a. Виведіть усі елементи списку з парними індексами.
# 	b. Знайти суму елементів всього списку.
# 	c. Знайти суму парних елементів списку та окремо непарних елементів списку.
# 	d. Виведіть значення найбільшого елемента у списку, а потім індекс цього елемента у списку.
# 		Якщо найбільших елементів кілька, виведіть індекс першого з них.

# from random import randint
#
# f_list = []
# for i in range(20):
#     f_list.append((randint(0, 666))) # за допомогою randint наповнюємо список числами
# print(f_list)
#
# even_number = f_list[::2] #парні індекси списку
# odd_number = f_list[1::2] #непарні елементи списку
# f_list_sum = sum(f_list) #сума усіх елементів списку
# f_list_max = max(f_list) #найбільше число списку
#
# print(even_number)
# print(odd_number)
# print(f_list_sum)
# print(f_list_max)
# print(sum(f_list[::2])) #сума парних елементів списку
# print(sum(f_list[1::2])) #сума непарних елементів списку

# 2. Написати алгоритм рішення fizzbuzz для 10 трійок чисел, які записані в файл (file_1.txt).
# 	Читайте із файлу перший рядок, берете із неї числа, рахуйте для них fizzbuzz, виводите.
# fizz = int(input('fizz: '))
# buzz = int(input('buzz: '))
# fizz_buzz = int(input('fizz_buzz: '))
#
# for fizz_buzz in range(1, fizz_buzz + 1):
#     if (fizz_buzz % fizz == 0) and (fizz_buzz % buzz == 0):
#         print('FB')
#     elif fizz_buzz % fizz == 0:
#         print('F')
#     elif fizz_buzz % buzz == 0:
#         print('B')
#     else:
#         print(fizz_buzz)


data = []
with open('file_1.txt') as f:
    for line in f:
        data.append([int(i) for i in line.split()])

for el in data:
    for q in range(1,el[2] + 1):
        if (el[2] % el[0] == 0) and (el[2] % el[1] == 0):
            print('FB')
        elif el[2] % el[0] == 0:
            print('F')
        elif el[2] % el[1] == 0:
            print('B')
        else:
            print(q)

# for el in data:
#     for q in range(el[2]):
#         if (el[2] % el[0] == 0) and (el[2] % el[1]):
#             print('FB')
#         elif el[2] % el[0] == 0:
#             print('F')
#         elif el[2] % el[1]:
#             print('B')
#         else:
#             print(q)
# for x, y, z in data:
#     for i in range(1, z + 1):
#         if (z % y == 0) and (z % x == 0):
#             print('FB')
#         elif z % x == 0:
#             print('F')
#         elif z % y == 0:
#             print('B')
#         else:
#             print(i)
    # if (z % x == 0) and (z % y == 0):
    #     print('FB')
    # elif z % x == 0:
    #     print('F')
    # elif z % y == 0:
    #     print('B')
    # else:
    #     print(data)



for j in range(1, (max(data[0]) + 1)):
    if (j % data[0][0] == 0) and (j % data[0][1] == 0):
        print('FB')
    elif j % data[0][0] == 0:
        print('F')
    elif j % data[0][1] == 0:
        print('B')
    else:
        print(j)

f = open('file_1.txt')
line = f.read().split()

print(line)






# 3. Створити список (наприклад, розміром 20 елементів) і заповнити елементами (для протсоти можна int або float).
# 	Сортувати список по 5 елементів.
# 	Тобто:
#             перші 5 елементів відсортувати за зростанням,
#             другу п'ятірку елементів за спаданням,
#             третю п'ятірку відсортувати за зростанням і11ttt
#             четверту п'ятірку за спаданням.
# Наприклад:
#             на початку [32,43,1,3,4,5,34,5,1,7,10,34,17,11]
#             на виході [1,3,4,32,43,34,5,7,5,1,10,11,17,34]
# Відповідь необхідно повернути в одному списку!
# 	*наприклад - мається на увазі, що це зразковий варіант розміру списку,
# а вам необхідно написати алгоритм, який зможе відсортувати список будь-якого розміру.

# from random import randint
#
# s_list = []
# for i in range(20):
#     s_list.append(randint(0, 999))
# print(s_list)
# sorted_list = sorted(s_list)
# print(len(sorted_list) // 4)
# print(sorted_list)
# print(sorted_list[:5])
# print(sorted_list[9:4:-1])
# print(sorted_list[10:15])
# print(sorted_list[:-6:-1])


