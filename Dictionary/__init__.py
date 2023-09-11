# <editor-fold desc="Задача 1">
import operator

# Task 1: Write a program that asks the user to enter a digit from 0 to 20, and prints the corresponding word.


# number_translation_dict = {0: 'zero',
#                            1: 'one',
#                            2: 'two',
#                            3: 'three',
#                            4: 'four',
#                            5: 'five',
#                            6: 'six',
#                            7: 'seven',
#                            8: 'eight',
#                            9: 'nine',
#                            10: 'ten',
#                            11: 'eleven',
#                            12: 'twelve',
#                            13: 'thirteen',
#                            14: 'fourteen',
#                            15: 'fifteen',
#                            16: 'sixteen',
#                            17: 'seventeen',
#                            18: 'eighteen',
#                            19: 'nineteen',
#                            20: 'twenty'} # Dictionary of numbers and their translations
#
#
# while True:
#     user_input = input("Enter a digit from 0 to 20: ")
#     try:
#         user_input = int(user_input)
#         if user_input in number_translation_dict:
#             print(number_translation_dict[user_input])
#         else:
#             print("Number is not in range from 0 to 20")
#     except ValueError:
#         print("Input is not a digit")


# </editor-fold>

# <editor-fold desc="Задача 2">

# NO.1 Task 2: Write a program that asks the user to enter age, gender and height, and prints the ideal weight.

# physical_activity_dict = {1: 'basal metabolic rate',
#                           2: 'sedentary - little or no exercise',
#                           3: 'light activity (1-3 times per week)',
#                           4: 'medium activity (3-5 times per week)',
#                           5: 'high activity (6-7 times per week)',
#                           6: 'very high activity (6-7 times per week + heavy physical work)'}
#
# BMR = None
#
# print("Basal Metabolic Rate Calculator")
# age = int(input("Please enter your age: "))
# gender = input("Please enter your gender (m/f): ")
# height = int(input("Please enter your height in cm: "))
# weight = float(input("Please enter your weight in kg: "))
# activity_level = int(input("Please enter your activity level (1-6): "))
#
# if gender == 'm':
#
#     BMR = 66.47 + (13.75 * weight) + (5.003 * height) - (6.755 * age)
#     if activity_level == 1:
#         BMR  = round(BMR, 2) * 1.375
#     elif activity_level == 2:
#         BMR = round(BMR, 2) * 1.55
#     elif activity_level == 3:
#         BMR = round(BMR, 2) * 1.725
#     elif activity_level == 4:
#         BMR = round(BMR, 2) * 1.9
#     else:
#         BMR = round(BMR, 2)
#
# else:
#
#     BMR = 655.1 + (9.563 * weight) + (1.85 * height) - (4.676 * age)
#
#     if activity_level == 1:
#         BMR = round(BMR, 2) * 1.375
#     elif activity_level == 2:
#         BMR = round(BMR, 2) * 1.55
#     elif activity_level == 3:
#         BMR = round(BMR, 2) * 1.725
#     elif activity_level == 4:
#         BMR = round(BMR, 2) * 1.9
#     else:
#         BMR = round(BMR, 2)
#
# print("Your BMR is: ", BMR)
# print("If you want to maintain your weight, you should consume: ", BMR, " calories per day")
# print("If you want to lose weight, you should consume: ", BMR - 500, " calories per day")
# print("If you want to gain weight, you should consume: ", BMR + 500, " calories per day")

# </editor-fold>

# <editor-fold desc="Задача 3">

# NO.1 Create a sample menu for a restaurant. The menu should have at least 5 items. Each item should have a name and
# a price.
#
# menu = {'pizza': 10,
#         'burger': 5,
#         'fries': 3,
#         'salad': 4,
#         'soup': 2}
#
# # NO.2 Print the menu to the console.
# customer_choice = input('Please enter your choice: ')
# total_price = 0
# while customer_choice != ' ':
#     if customer_choice in menu:
#         total_price += menu[customer_choice]
#         print('Your total price is: ', total_price)
#     else:
#         print('Your choice is not in the menu')
#     customer_choice = input('Please enter your choice: ')

# </editor-fold>

# <editor-fold desc="Задача 4">
#
# cities = {'Sofia': 0,
#           'Plovdiv': 0,
#           'Varna': 0,
#           'Burgas': 0}
#
# # NO.1 Enter rain data for each city. The program should ask the user to enter the amount of rain for a given city n
# # times until the user press enter.
#
# # NO.2 Print the total amount of rain for each city to the console.
#
# while True:
#     user_input = input('Please enter city name: ')
#
#     # if the user presses enter, the program should stop but before that it should print the total amount of rain for
#     # each city.
#
#     if user_input == "":
#         print(cities)
#         break
#     if user_input in cities:
#         rain_quantity_mm = input('Please enter rain quantity in mm: ')
#         cities[user_input] += int(rain_quantity_mm)
#     else:
#         print('City is not in the list')


# </editor-fold>

# <editor-fold desc="Задача 5">

# dict_1 = {'a': 1,
#           'b': 2,
#           'c': 3
#           }
#
# dict_2 = {'x': 2,
#           'b': 2,
#           'c': 3
#           }
#
# keys_in_dict1_not_in_dict2 = list(set(dict_1.keys()) - set(dict_2.keys()))
# keys_in_dict2_not_in_dict1 = list(set(dict_2.keys()) - set(dict_1.keys()))
#
# list_of_values_diff = []
# new_dict = {}
#
# for key in keys_in_dict1_not_in_dict2:
#     # check if the keys are the same if they are not please go on do not throw an error
#
#     if key == dict_2.get(key, None):
#
#         if dict_1[key] != dict_2.get(key, None):
#
#             list_of_values_diff.append(dict_1.get(key, None))
#             list_of_values_diff.append(dict_2.get(key, None))
#             new_dict[key] = list_of_values_diff
#
#         else:
#
#             new_dict[key] = list_of_values_diff
#
#     else:
#
#         list_of_values_diff.append(dict_1.get(key, None))
#         list_of_values_diff.append(dict_2.get(key, None))
#         new_dict[key] = list_of_values_diff
#
#
#
# for key in keys_in_dict2_not_in_dict1:
#     # check if the keys are the same if they are not please go on do not throw an error
#
#     if key == dict_1.get(key, None):
#
#         if dict_2[key] != dict_1.get(key, None):
#             list_of_values_diff.append(dict_2.get(key, None))
#
#             new_dict[key] = list_of_values_diff
#
#         else:
#
#             new_dict[key] = list_of_values_diff
#
#     else:
#
#         list_of_values_diff.append(dict_2.get(key, None))
#         list_of_values_diff.append(dict_1.get(key, None))
#         new_dict[key] = list_of_values_diff
#
# print(new_dict)

# </editor-fold>

# <editor-fold desc="Задача 6">
# from collections import Counter
#
# bulgarian_english_dictionary = {
#     "car": "кола",
#     "dog": "куче",
#     "cat": "котка",
#     "table": "маса",
#     "carr": "кола",
# }
#
# double_key_list = []
#
#
# user_input = input("Въведете дума: ")
#
# counter = Counter(bulgarian_english_dictionary.values())
#
# # check if user_input is duplicated
# if counter[user_input] > 1:
#     # iterate over items in original dictionary
#     for key, value in bulgarian_english_dictionary.items():
#         # check if value is equal to user_input
#         if value == user_input:
#             double_key_list.append(key)
#
# print(double_key_list)

# </editor-fold>

# <editor-fold desc="Задача 7">

#
# from collections import Counter
# import random
#
# # Step 1: Generate all possible sums
# sums = [i + j for i in range(1, 7) for j in range(1, 7)]
#
# # Step 2: Count occurrences of each sum
# counter = Counter(sums)
#
# # Step 3: Calculate probabilities
# probabilities = {k: v / len(sums) for k, v in counter.items()}
#
# dict_sum_dices_prob = {}
#
#
# for i in range(1000):
#
#     dice_1 = random.randint(1, 6)
#     dice_2 = random.randint(1, 6)
#
#     dices_sum = dice_1 + dice_2
#     probability = probabilities[dices_sum]
#
#     dict_sum_dices_prob[dices_sum] = probability
#
# for i in dict_sum_dices_prob:
#     print(i, round(dict_sum_dices_prob[i], 2) )
#

# </editor-fold>

# <editor-fold desc="Задача 8">

# dictionary = {'a': 0,
#               'b': 0,
#               'c': 0,
#               'd': 0,
#               'e': 0,
#               'f': 0,
#               'g': 0,
#               'h': 0,
#               'i': 0,
#               'j': 0,
#               'k': 0,
#               'l': 0,
#               'm': 0,
#               'n': 0,
#               'o': 0,
#               'p': 0,
#               'q': 0,
#               'r': 0,
#               's': 0,
#               't': 0,
#               'u': 0,
#               'v': 0,
#               'w': 0,
#               'x': 0,
#               'y': 0,
#               'z': 0}  # Dictionary of letters and their occurrences in the string
#
# user_input = input('Please enter a string: ')
#
# for i in user_input:
#     if i in dictionary:
#         dictionary[i] += 1
#
# duplicated_letters = [letter for letter in dictionary if dictionary[letter] > 1]
#
# for i in user_input:
#     if i not in duplicated_letters:
#         print(f'{i}', end='')
#
# print()

# </editor-fold>

# <editor-fold desc="Задача 9">

# import enchant
# d = enchant.Dict("en_US")
#
# user_input = input('Please enter a string: ')
# reversed_string = user_input[::-1]
#
# if d.check(reversed_string):
#     print("This is an English word and is anagram of the input string")
# else:
#     print("This is not an English word and is not an anagram of the input string")
#
# </editor-fold>

# <editor-fold desc="Задача 10">

# dict_letter_points = {1: ['a', 'e', 'i', 'l', 'n', 'o', 'r', 's', 't', 'u'],
#                       2: ['d', 'g'],
#                       3: ['b', 'c', 'm', 'p'],
#                       4: ['f', 'h', 'v', 'w', 'y'],
#                       5: ['k'],
#                       8: ['j', 'x'],
#                       10: ['q', 'z']}
#
# user_input = input('Please enter a string: ')
#
# total_points = 0
#
# for i in user_input:
#     for key in dict_letter_points:
#         if i in dict_letter_points[key]:
#             total_points += key
#
# print(total_points)

# </editor-fold>

# <editor-fold desc="Задача 11">

# dictionary = {'B': [1,  2,  3,  4,  5,  6,  7,  8,  9,  10, 11, 12, 13, 14, 15],
#               'I': [17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31],
#               'N': [32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46],
#               'G': [47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61],
#               'O': [62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76]}
#
# for key in dictionary:
#     print(key.rjust(5), end='')
# print()
#
# # Print the values
# for i in range(len(dictionary['B'])): # assuming all lists have the same length
#     for key in dictionary:
#         print(str(dictionary[key][i]).rjust(5), end='')
#     print()

# </editor-fold>

# <editor-fold desc="Задача 12">

# dictionary = {'a': 0,
#               'b': 0,
#               'c': 0,
#               'd': 0,
#               'e': 0,
#               'f': 0,
#               'g': 0,
#               'h': 0,
#               'i': 0,
#               'j': 0,
#               'k': 0,
#               'l': 0,
#               'm': 0,
#               'n': 0,
#               'o': 0,
#               'p': 0,
#               'q': 0,
#               'r': 0,
#               's': 0,
#               't': 0,
#               'u': 0,
#               'v': 0,
#               'w': 0,
#               'x': 0,
#               'y': 0,
#               'z': 0}  # Dictionary of letters and their occurrences in the string
#
# user_input = input('Please enter a string: ')
#
# for i in user_input:
#     if i in dictionary:
#         dictionary[i] += 1
#
# duplicated_letters = [letter for letter in dictionary if dictionary[letter] > 1]
#
# for i in user_input:
#     if i not in duplicated_letters:
#         print(f'{i}', end='')
#
# print()

# </editor-fold>

# <editor-fold desc="Задача 13">

# capital_letters_ASCII = [i for i in range(65, 91)]
#
# user_input = input('Please enter a list of words with capital letters, separated with commas: ')
#
# dict_of_words_and_number_of_capital_letters = {}
#
#
# for word in user_input.split(','):
#     capitally_letter_counter = 0
#     for letter in word:
#         if ord(letter) in capital_letters_ASCII:
#             capitally_letter_counter += 1
#             dict_of_words_and_number_of_capital_letters[word] = capitally_letter_counter
#
#
# print(dict_of_words_and_number_of_capital_letters)

# </editor-fold>

# <editor-fold desc="Задача 14">

# dictionary with sales for each quarter of the year {"Q4”: 250, “Q1”: 300, “Q2”: 150, “Q3”: 0}
# sales = {"Q4": 250, "Q1": 300, "Q2": 150, "Q3": 0}
#
# print(sales)
#
# sorted_dict = dict(sorted(sales.items(), key=operator.itemgetter(1), reverse=True))
# new_dict = {}
#
# for key in sorted_dict:
#
#     if sorted_dict[key] != 0:
#         number_of_symbols = sorted_dict[key] // 50
#         new_temp_key = key + "|" + "#" * number_of_symbols
#         new_dict[new_temp_key] = sorted_dict[key]
#
# print(new_dict)

# </editor-fold>

# <editor-fold desc="Задача 15">

# client_base = {}
#
# while True:
#
#     client_name = input("Please enter a client: ")
#     client_order = input("Please enter an order price: ").split(",")
#
#     print("Would you like to add another client y/n: ")
#     user_input = input()
#     if user_input == "n":
#         client_base[client_name] = client_order
#         break
#     else:
#         client_base[client_name] = client_order
#         continue
#
# min_price_for_discount = 50
# min_orders_for_discount = 3
# discount = 0.2
#
# customer_with_discounted_price = {}
# new_discounted_price = 0
#
#
# for key in client_base:
#     if len(client_base[key]) >= min_orders_for_discount:
#         if sum([int(i) for i in client_base[key]]) >= min_price_for_discount:
#             new_discounted_price = sum([int(i) for i in client_base[key]]) * (
#                 1 - discount
#             )
#             customer_with_discounted_price[key] = new_discounted_price
#
#
# print(customer_with_discounted_price)

# </editor-fold>

# <editor-fold desc="Задача 16">

# competitors = {"George": 96, "Emily": 95, "Susan": 93, "Jane": 89, "Brett": 82}
#
# # Sort the dictionary by value in descending order
# sorted_dict = {
#     k: v for k, v in sorted(competitors.items(), key=lambda item: item[1], reverse=True)
# }
#
# competitor_name = "Jane"
#
# ranked_competitors = {}
# rank = 0
# prev_score = None
#
# for key, value in sorted_dict.items():
#     if value != prev_score:
#         rank += 1
#     ranked_competitors[key] = rank
#     prev_score = value
#
# print(ranked_competitors)
# print(ranked_competitors[competitor_name])

# </editor-fold>

# <editor-fold desc="Задача 17">

# student_scores = {
#     "John": [100, 90, 80],  # average score = 90
#     "Bob": [100, 70, 80],  # average score = 83.33
# }
#
# # Calculate average scores and store them in the dictionary
# for student, scores in student_scores.items():
#     avg_score = sum(scores) / len(scores)
#     student_scores[student] = [scores, avg_score]
#
#
# student_with_highest_avg_score = max(student_scores, key=student_scores.get)
# print(student_with_highest_avg_score)

# </editor-fold>
