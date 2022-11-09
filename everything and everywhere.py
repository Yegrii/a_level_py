
str_2 = 'cvcbcbnvm'

if len(str_2) <= 10:
    if str_2.isupper():
        str_2 = str_2.replace(str_2[-3:], str_2[-3:].lower())
        str_2 = str_2[:(len(str_2) - 3) // 2] + str_2[-3:] + str_2[(len(str_2) - 3) // 2:-3]
        print('Upper string: ', str_2)
    elif str_2.islower():
        str_2 = str_2.replace(str_2[-3:], str_2[-3:].upper())
        str_2 = str_2[:(len(str_2) - 3) // 2] + str_2[-3:] + str_2[(len(str_2) - 3) // 2:-3]
        print('Lower string: ', str_2)
else:
    print('ERROR')



