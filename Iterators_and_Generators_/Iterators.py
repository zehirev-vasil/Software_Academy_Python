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

# <editor-fold desc="Задача 7">

user_input = input("Enter a word: ")


def gen_word(word, is_vowel):
    vowels = ["a", "e", "i", "o", "u"]

    for i in word:
        if (i in vowels) == is_vowel:
            yield i


print(f'List of vowels: {list(gen_word(user_input, True))}')
print(f'List of consonants: {list(gen_word(user_input, False))}')
