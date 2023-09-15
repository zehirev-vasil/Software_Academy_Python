# <editor-fold desc="Задача 1">
# 1. Write a Python program to create a tuple with different data types.
#
#
# my_list = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
# sorted_list = sorted(my_list, key=lambda x: x[-1])
# print(sorted_list)
from cmath import sqrt

# </editor-fold>

# <editor-fold desc="Задача 2">

# import itertools
#
# data = ['A', 'B', 'C']
#
# symbols = ['-', '+']


# for r in range(1, len(data) + 1):
#     combinations = itertools.combinations(data, r)
#
#     for combo in combinations:
#         print(''.join(combo))
#
#         if len(''.join(combo)) > 1:
#             for i in symbols:
#                 print(i.join(combo)

# </editor-fold>

# <editor-fold desc="Задача 3">

# from collections import Counter
#
# fruits = ["apple", "banana", "cherry", "apple"]
#
# # Count the occurrences of each element in the list
# counter = Counter(fruits)
#
# # Find elements that appear more than once
# duplicates = [item for item, count in counter.items() if count > 1]
# uniques = [item for item, count in counter.items() if count == 1]
#
# print(duplicates)
# print(f'Count of duplicates: {len(duplicates)}')
# print(uniques)
# print(f'Count of uniques: {len(uniques)}')
#
# tuple_dup_uniq = (len(duplicates), len(uniques))

# </editor-fold>

# <editor-fold desc="Задача 4">

# a = {1, 2}; b = {2, 3}
#
# print(f'The union | is: {a.union(b)}')
#
# print(f'The intersection & is: {a.intersection(b)}')
#
# print(f'The difference - is: {a.difference(b)}')
#
# print(f'The symmetric difference ^ is: {a.symmetric_difference(b)}')

# </editor-fold>

# <editor-fold desc="Задача 5">

# x1 = 0
# x2 = int(input('Enter x2: '))
#
# y1 = 0
# y2 = int(input('Enter y2: '))
#
# distance_formula = sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
#
# print(f'The distance between points ({x1}, {y1}) and ({x2}, {y2}) is: {distance_formula}')

# </editor-fold>

# <editor-fold desc="Задача 6">

# x1 = int(input('Enter x1: '))
# y1 = int(input('Enter y1: '))
#
# x2 = int(input('Enter x2: '))
# y2 = int(input('Enter y2: '))
#
# distance_formula = sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
#
# print(f'The distance between points ({x1}, {y1}) and ({x2}, {y2}) is: {distance_formula}')

# </editor-fold>

# <editor-fold desc="Задача 7">
#
# x1 = int(input('Enter x1: '))
# y1 = int(input('Enter y1: '))
# z1 = int(input('Enter z1: '))
#
# x2 = int(input('Enter x2: '))
# y2 = int(input('Enter y2: '))
# z2 = int(input('Enter z2: '))
#
# distance_formula = sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2)
#
# print(f'The distance between points ({x1}, {y1}, {z1}) and ({x2}, {y2}, {z2}) is: {distance_formula}')

# </editor-fold>