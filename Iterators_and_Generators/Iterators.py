# <editor-fold desc="Задача 1">

# gen = (i for i in range(1, 11) if i % 2 == 0)
#
# for i in gen:
#     print(i, end=" ")

# </editor-fold>

# <editor-fold desc="Задача 2">

# def gen(n):
#     for i in range(1, n + 1):
#         if i % 2 == 0:
#             yield i
#
#
# print(gen(10))
#
# print(list(gen(10)))
# print(tuple(gen(10)))
# print(type(gen(10)))
#
# for i in gen(10):
#     print(i, end=" ")
#     print(type(i))

# </editor-fold>

# <editor-fold desc="Задача 3">

# what are prime numbers?
# prime numbers are numbers that can be divided only by one and themselves.

# def generate_primes(n):
#     for num in range(2, n + 1):
#         if all(num % i != 0 for i in range(2, num)):
#             yield num
#
#
# print(list(generate_primes(10)))

# </editor-fold>

# <editor-fold desc="Задача 4">

# my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
# iterator = iter(my_list)
#
# print(type(iterator))  # prints <class 'list_iterator'>
#
#
# while True:
#
#     try:
#         tmp = next(iterator)
#         print(tmp if tmp % 2 == 0 else "")
#     except StopIteration:
#         break

# </editor-fold>

# <editor-fold desc="Задача 5">

# my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
# iterator = iter(my_list)
#
# print(type(iterator))  # prints <class 'list_iterator'>
#
#
# while True:
#
#     try:
#         tmp = next(iterator)
#         print(tmp if tmp % 2 != 0 else "")
#     except StopIteration:
#         break

# </editor-fold>

# <editor-fold desc="Задача 6">

# list_num = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
#
#
# def gen_neg(n, sign):
#
#     list_of_neg = []
#     list_of_pos = []
#
#     iterator = iter(n)
#
#     while True:
#         try:
#             tmp = next(iterator)
#             if tmp < 0:
#                 list_of_neg.append(tmp)
#             else:
#                 list_of_pos.append(tmp)
#         except StopIteration:
#             break
#
#     if sign == "-":
#         return list_of_neg
#     elif sign == "+":
#         return list_of_pos
#     else:
#         return "Wrong sign"
#
#
# print(gen_neg(list_num, "-"))
# print(gen_neg(list_num, "+"))


# </editor-fold>

# <editor-fold desc="Задача 8">

# user_input = input("Enter a word: ")
#
#
# def gen_word(word, is_vowel):
#     vowels = ["a", "e", "i", "o", "u"]
#
#     for i in word:
#         if (i in vowels) == is_vowel:
#             yield i
#
#
# print(f'List of vowels: {list(gen_word(user_input, True))}')
# print(f'List of consonants: {list(gen_word(user_input, False))}')

# </editor-fold>

# <editor-fold desc="Задача 9">

# user_input = input("Enter a word: ")
#
#
# def iter_word(word, is_vowel):
#     iterator = iter(word)
#     vowels = ["a", "e", "i", "o", "u"]
#
#     list_of_vowels = []
#     list_of_consonants = []
#
#     while True:
#         try:
#             tmp = next(iterator)
#             if (tmp in vowels) == is_vowel:
#                 list_of_vowels.append(tmp)
#             else:
#                 list_of_consonants.append(tmp)
#         except StopIteration:
#             break
#
#     if is_vowel:
#         return list_of_vowels
#     else:
#         return list_of_consonants
#
#
# print(f'List of vowels: {iter_word(user_input, True)}')
# print(f'List of consonants: {iter_word(user_input, False)}')

# </editor-fold>

# <editor-fold desc="Задача 10">

# list_1 = [1, 2, 3, 4, 5]
# list_2 = [10, 9, 8, 7, 6]
#
# combined_list = list_1 + list_2
#
# n = len(combined_list)
#
# for i in range(n):
#
#     for j in range(n - i - 1):
#
#         if combined_list[j] > combined_list[j + 1]:
#             combined_list[j], combined_list[j + 1] = combined_list[j + 1], combined_list[j]
#
#
# print(combined_list)

# </editor-fold>

# <editor-fold desc="Задача 11">

# start = input("Enter start: ")
# step = input("Enter step: ")
# count_of_numbers = input("Enter count of numbers: ")
#
# start = int(start)
# step = int(step)
# count_of_numbers = int(count_of_numbers)
#
#
# # formula for arithmetic progression: a(n) = a(1) + (n - 1) * d
# def gen(start_ar_prog, step_ar_prog, count_of_numbers_ar_prog):
#     for i in range(start_ar_prog, start_ar_prog + step_ar_prog * count_of_numbers_ar_prog, step_ar_prog):
#         yield i
#
#
# print(list(gen(start, step, count_of_numbers)))

# </editor-fold>

# <editor-fold desc="Задача 12">

# formula for geometric progression: a(n) = a(1) * q ** (n - 1)

# start = input("Enter start: ")
# step = input("Enter step: ")
# count_of_numbers = input("Enter count of numbers: ")
#
# start = int(start)
# step = int(step)
# count_of_numbers = int(count_of_numbers)
#
#
# def gen(start_geo_prog, step_geo_prog, count_of_numbers_geo_prog):
#     for i in range(start_geo_prog, count_of_numbers_geo_prog):
#         j = start_geo_prog * step_geo_prog ** (i - 1)
#         yield j
#
#
# print(list(gen(start, step, count_of_numbers)))

# </editor-fold>

# <editor-fold desc="Задача 13">
#
# list_one = [1, 2, 3, 4, 5]
# list_two = [6, 7, 8, 9, 10]
#
# decart_list = []
#
# for i in list_one:
#     for j in list_two:
#         decart_list.append((i, j))
#
# print(decart_list)

# </editor-fold>

# <editor-fold desc="Задача 14">

# import itertools
#
# list_one = [1, 2, 3, 4, 5]
# list_two = [6, 7, 8, 9, 10]
#
# decart_list = []
#
# print(list(itertools.product(list_one, list_two)))

# </editor-fold>
