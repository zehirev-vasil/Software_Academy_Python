# <editor-fold desc="1">

# my_list = [1, 2, 5, 9, 10]
#
# num_to_find = 5
#
#
# def find_num(mylist, numtofind):
#     for idx, val in enumerate(mylist):
#         #print(idx, val)
#         if val == numtofind:
#             return idx
#
#
# print('The number is at idx: ', end='')
# print(find_num(my_list, num_to_find))
#
#

# </editor-fold>

# <editor-fold desc="3">

# F(n) = F(n-1) + F(n-2)
# please do not show a solution for this task.
# def Fib(n):
#     if n == 0 or n == 1:
#         return n
#     else:
#         return Fib(n - 1) + Fib(n - 2)
#
#
# print('The fib num is: {0}'.format(Fib(5)))

# </editor-fold>

# <editor-fold desc="4">

# n! = n × (n−1)!

# num = 5
#
#
# def Fac(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n * Fac(n - 1)
#
#
# print('The result is {}'.format(Fac(5)))

# </editor-fold>

# <editor-fold desc="5">
#
# user_basket = []
#
#
# def Add(item):
#     user_basket.append(item)
#
#
# def Remove(item):
#     user_basket.remove(item)
#
#
# def Clear():
#     user_basket.clear()
#
#
# def Show():
#     print(user_basket)
#
#
# def Quit():
#     exit(0)
#
#
# while True:
#
#     print('Please choose an option from the given menu: ')
#     user_input = input('Add \nRemove \nClear \nShow \nQuit \n')
#
#     if user_input == 'Add':
#         tmp = input('Please add an item to your basket:\n')
#         Add(tmp)
#     elif user_input == 'Remove':
#         tmp = input('Please write an item to to be removed:\n')
#         Remove(tmp)
#     elif user_input == 'Clear':
#         user_basket.clear()
#     elif user_input == 'Show':
#         Show()
#     else:
#         Quit()


# </editor-fold>

# <editor-fold desc="6">

# tuple_list = [(1, 10), (2, 20), (3, 30), (5, 50), (4, 40)]
#
# print(tuple_list)
#
# sorted_tuple_list = sorted(tuple_list, key=lambda x: x[1],reverse=True)
#
# print(sorted_tuple_list)

# </editor-fold>

# <editor-fold desc="7">

# dic1 = [{'A': 1}, {'B': 2}, {'C': 3}]
# dic2 = [{'D': 4}, {'E': 5}, {'F': 6}]
#
# values = list(map(lambda x: list(x.values()), dic1))
#
# print(values)


# </editor-fold>

# <editor-fold desc="8">

# my_list = [1, 2, 3, 4, 5]
#
# even = list(filter(lambda x: x % 2 == 0, my_list))
# odd = list(filter(lambda x: x % 2 != 0, my_list))
# print(even)
# print(odd)


# </editor-fold>
