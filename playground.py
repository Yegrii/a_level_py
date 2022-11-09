
# first_input = str(input("Input First Word: "))
# second_input = str(input('Second input: '))
# third_input = str(input('Third Input: '))
#
# if len(first_input) or len(second_input) or len(third_input) % 2 == 0:
#     mid_lett = len(first_input), len(second_input), len(third_input) // 2
#     print(first_input[mid_lett - 1], first_input[mid_lett], second_input[mid_lett - 1], second_input[mid_lett], third_input[mid_lett - 1], third_input[mid_lett])
# else:
#     mid_lett_2 = len(first_input), len(second_input), len(third_input) // 2
#     print(first_input[mid_lett_2], second_input[mid_lett_2], third_input[mid_lett_2])
#

# f_input = str(input('First: '))
# s_input = str(input('Second: '))
# t_input = str(input('Third: '))
#
# # if len(f_input) or len(s_input) or len(t_input) % 2 == 0:
# #     mid_f = len(f_input) // 2
# #     mid_s = len(s_input) // 2
# #     mid_t = len(t_input) // 2
# #     print(f'Your middle letters are: {f_input[mid_f - 1]}{f_input[mid_f]}, {s_input[mid_s - 1]}{s_input[mid_s]}, {t_input[mid_t - 1]}{t_input[mid_t]}')
# # else:
# #     mid_f = len(f_input) // 2
# #     mid_s = len(s_input) // 2
# #     mid_t = len(t_input) // 2
# #     print(f'Your middle letters are: {f_input[mid_f]} {s_input[mid_s]} {t_input[mid_t]}')
# if len(f_input) % 2 == 0:
#     mid_f = len(f_input) // 2
#     print(f_input[mid_f - 1], f_input[mid_f])
# elif len(f_input) % 2 != 0:
#     mid_f = len(f_input) // 2
#     print(f_input[mid_f])
#
# if len(s_input) % 2 == 0:
#     mid_s = len(s_input) // 2
#     print(s_input[mid_s - 1], s_input[mid_s])
# elif len(s_input) % 2 != 0:
#     mid_s = len(s_input) // 2
#     print(s_input[mid_s])
#
# if len(t_input) % 2 == 0:
#     mid_t = len(t_input) // 2
#     print(t_input[mid_t - 1], t_input[mid_t])
# elif len(t_input) % 2 != 0:
#     mid_t = len(t_input) // 2
#     print(t_input[mid_t])

# def mid_letters(frst, scnd, trd):
#     if len(frst) % 2 == 0:
#         mid_f = len(frst) // 2
#         print(frst[mid_f - 1], frst[mid_f])
#     else:
#         mid_f = len(frst) // 2
#         print(frst[mid_f])
#     if len(scnd) % 2 == 0:
#         mid_s = len(scnd) // 2
#         print(scnd[mid_s - 1], scnd[mid_s])
#     else:
#         mid_s = len(scnd) // 2
#         print(scnd[mid_s])
#     if len(trd) % 2 == 0:
#         mid_t = len(trd) // 2
#         print(trd[mid_t - 1], trd[mid_t])

# def letters(let):
#     if len(let) % 2 == 0:
#         i = len(let) // 2
#         return f'Your letters is: {let[i - 1]}{let[i]}'
#     else:
#         i = len(let) // 2
#         return f'Your letter is: {let[i]}'

# str_1 = 'Qwertyasdfghzx'
# str_1 = str_1[len(str_1)//2:] + str_1[:len(str_1)//2].replace('tya', 'TYA')
# # str_1 = str_1.replace('tya', 'TYA')
# print(str_1)
#
# str_2 = 'QWEASDZXCK'
# str_2 = str_2.replace('XCK', 'xck')
# str_2 = str_2[:2] + str_2[-3:] + str_2[2:7]
# print(str_2)

# str_2 = str_2.replace('XCK', 'xck')
# str_l = list(str_2)
# print(str_l)
# str_l[-3:] = str_l[-8:-5]

# print(str_l)

# text = 'Foobar'
# l = list(text)
# l[2], l[4] = l[4], l[2]
# # ''.join(l)
# print(l)
# 	print("#",end="")
# 	print(" ",end="")
# 	print("") #перехід на новий рядок, якщо треба.

# n = int(input())
# for i in range(n):
#     for j in range(n):
#         if i == 0 or j == 0 or i == n-1 or j == n-1:
#             print("#",end="")
#         else:
#             print(" ",end="")
#     print("")

# for i in range(5):
#     for e in range(5):
#         if i == 0 or e == 0 or i == 4 or e == 4:
#             print('#', end='')
#         else:
#             print(' ', end='')
#     print('')


# str_1 = 'Qwertyasdfghzx'
# if len(str_1) >= 5 and len(str_1) <= 15:
#     str_1 = str_1[len(str_1)//2:] + str_1[:len(str_1)//2].replace('tya', 'TYA')
#     print("Changed string: ", str_1)
# else:
#     print('This string is too short or too long')
#
#
# str_2 = 'QWEASDZXCK'
#
# if len(str_2) <= 10:
#     if str_2.isupper():
#         str_2 = str_2.replace(str_2[-3:], str_2[-3:].lower())
#         str_2 = str_2[:(len(str_2) - 3) // 2] + str_2[-3:] + str_2[(len(str_2) - 3) // 2:-3]
#         print('Upper string: ', str_2)
#     elif str_2.islower():
#         str_2 = str_2.replace(str_2[-3:], str_2[-3:].upper())
#         str_2 = str_2[:(len(str_2) - 3) // 2] + str_2[-3:] + str_2[(len(str_2) - 3) // 2:-3]
#         print('Lower string: ', str_2)
# else:
#     print('ERROR')