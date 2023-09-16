# <editor-fold desc="Задача 1">
import random

# my_list = []
#
# user_input = int(input("Please enter a digit: "))
#
# my_list.append(user_input)
#
# while user_input != 0:
#     user_input = int(input("Please enter a digit: "))
#     my_list.append(user_input)
#
# # print (my_list) with every value on new line
# my_list.pop()
#
# my_list.sort(reverse=True)
#
# print("\n".join(str(my_list)))

# </editor-fold>

# <editor-fold desc="Задача 2">

# try: block must check if a user has entered at least 4 digits, separated by comma. The must be converted to a list.
# If a user has entered less than 4 digits, separated by comma, the program must ask to enter more digits, separated by comma.
# if a user has entered not a digit , the program must ask to enter a digit.
#
# numbers = []
# while len(numbers) < 4:
#     try:
#         numbers = input("Въведете списък от числа, които трябва да са поне 4: ").split(
#             ","
#         )
#         numbers = [int(number) for number in numbers]
#     except ValueError:
#         print("Невалиден списък от числа.")
#         numbers.clear()
#         numbers = input("Въведете отново списък от 4 или повече числа: ").split(",")
#         numbers = [int(number) for number in numbers]
#
# # Премахване на най-крайните стойности.
# new_numbers = []
# for number in numbers:
#     if str(number) not in str(min(numbers)) and str(number) not in str(max(numbers)):
#         new_numbers.append(number)
#
#
# # Отпечатване на оригиналния и новия списък.
# print("Оригинален списък:", numbers)
# print("Нов списък:", new_numbers)


# </editor-fold>

# <editor-fold desc="Задача 3">
#
# my_list = []
# user_input = input("Please enter a word: ")
#
# while user_input != '':
#     user_input = input("Please enter a word: ")
#     my_list.append(user_input)
#
# modified_list = []
#
# for i in my_list:
#     if i not in modified_list:
#         modified_list.append(i)
#
#
# print(modified_list)

# </editor-fold>

# <editor-fold desc="Задача 4">

# user_inputs = []
# neg_num_list = []
# pos_num_list = []
# zero_num_list = []
#
#
# while True:
#     user_input = input("Please enter something: ")
#     if user_input == "":
#         break
#     else:
#         user_inputs.append(user_input)
#
#
# for i in user_inputs:
#     if int(i) < 0:
#         neg_num_list.append(int(i))
#     elif int(i) > 0:
#         pos_num_list.append(int(i))
#
#     else:
#         zero_num_list.append(int(i))
#
# print("Negative numbers: ", neg_num_list, end=" ")
# print("Zero numbers: ", zero_num_list, end=" ")
# print("Positive numbers: ", pos_num_list, end=" ")

# </editor-fold>q

# <editor-fold desc="Задача 5">

# NO.1 create a list of 6 random numbers in range 1-49
# NO.2 create a list of 6 user input numbers in range 1-49
# NO.3 compare the lists and print the amount matches.

# random_numbers = []
# user_numbers = []
# matches = 0
#
# for i in range(6):
#     random_numbers.append(random.randint(1, 49))
#
# for i in range(6):
#     user_input = int(input("Please enter a number: "))
#     user_numbers.append(user_input)
#
# for i in user_numbers:
#     if i in random_numbers:
#         matches += 1
#
# print("Random numbers: ", random_numbers)
# print("User numbers: ", user_numbers)
# print("Matches: ", matches)

# </editor-fold>

# <editor-fold desc="Задача 6">

# input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#
# sublist = []
#
# for i in range(len(input_list)):
#     for j in range(i + 1, len(input_list) + 1):
#         sublist.append(input_list[i:j])
#
# print(sublist)

# </editor-fold>

# <editor-fold desc="Задача 7">

# user_input = input("Please enter a list of numbers, separated with comma: ")
# user_input = [int(i) for i in user_input.split(",")]
#
# list_of_numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#
# max_counter = 0
# most_frequent_number = 0
#
# for i in list_of_numbers:
#     counter = 0
#     for j in user_input:
#         if i == j:
#             counter += 1
#     if counter > max_counter:
#         max_counter = counter
#         most_frequent_number = i
#
# print("Most frequent number is: ", most_frequent_number)
# print("It appears ", max_counter, " times.")

# </editor-fold>

# <editor-fold desc="Задача 8">

# list_of_numbers = [5, 4, 3, 1, 2, 3]
#
# # Find the first occurrence of 1 in the list
# start_index = list_of_numbers.index(1)
#
# sequence = [list_of_numbers[start_index]]
#
# for i in range(start_index, len(list_of_numbers) - 1):
#     if list_of_numbers[i + 1] - list_of_numbers[i] == 1:
#         sequence.append(list_of_numbers[i + 1])
#
# print(sequence)

# </editor-fold>

# <editor-fold desc="Задача 9">

# for i in range(1, 5):
#     print(f"{i} ", end=" ")
#     for j in range(i + 4, i + 13, 4):
#         print(f"{j} ", end=" ")
#     print()

# </editor-fold>
