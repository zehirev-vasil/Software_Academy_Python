# <editor-fold desc="Задача 1">
# for i in range(1500, 2700):
#     if i % 7 == 0 and i % 5 == 0:
#         print(i)
# </editor-fold>
import string

# <editor-fold desc="Задача 2">

# total_sum = 0
#
# for i in range(1, 6):
#     tmp = int(input(f"Please enter a digit: "))
#     total_sum += tmp
#
# print(f"Total sum is {total_sum}")
# </editor-fold>

# <editor-fold desc="Задача 3">

# for i in range(1, 6):
#     for j in range(1, i + 1):
#         print("* ", end="")
#     print()
#
# for i in range(4, 0, -1):
#     for j in range(1, i + 1):
#         print("* ", end="")
#     print()

# </editor-fold>

# <editor-fold desc="Задача 4">

# user_input = input("Please enter a word: ")
#
# for i in range(len(user_input) - 1, -1, -1):
#     print(user_input[i], end="")

# </editor-fold>

# <editor-fold desc="Задача 5">

# user_input = input("Please enter list of numbers: ")
#
# user_input = user_input.split(",")
# even_numbers = [int(i) for i in user_input if int(i) % 2 == 0]  # list comprehension
# odd_numbers = [int(i) for i in user_input if int(i) % 2 != 0]  # list comprehension
#
# # Count of element in both lists
# print(f"Count of even numbers is {len(even_numbers)}")
# print(f"Count of odd numbers is {len(odd_numbers)}")

# </editor-fold>

# <editor-fold desc="Задача 6">

# num = 0
#
# while num <= 10:
#     if (num % 3 == 0 or num % 6 == 0) and num > 0:
#         num += 1
#         continue
#     else:
#         print(num)
#         num += 1

# </editor-fol

# <editor-fold desc="Задача 7">

# <editor-fold desc="Задача 7">

# num_a = 0
# num_b = 1
#
# while num_a < 50:
#     print(num_a)
#     num_a, num_b = num_b, num_a + num_b  # swap values

# </editor-fold>

# <editor-fold desc="Задача 8">

# for i in range(7):
#     for j in range(5):
#
#         # NO. Condition 1 – print first row.
#         if i == 0 and 0 < j < 4:
#             print("*", end="")
#         # NO. Condition 2 – print 2, 3, 5, 6, 7 rows.
#         elif 0 < i < 6 and i != 3:
#             if j == 0 or j == 4:
#                 print("*", end="")
#             else:
#                 print(" ", end="")
#         # NO. Condition 3 – print 2, 3, 5, 6, 7 rows.
#         elif i == 3:
#             print("*", end="")
#         else:
#             print(" ", end="")
#
#     print()

# <editor-fold desc="Задача 9">

# for i in range(1, 10):
#     for j in range(1, i + 1):
#         print(i, end="")
#     print()

# </editor-fold>

# <editor-fold desc="Задача 10">

# n = int(input("Enter a single-digit number: "))
#
# sum = 0
# for i in range(1, n+1):
#     product = 1
#     for j in range(i, 2*i+1):
#         product *= j
#     sum += product
# print(sum)

# </editor-fold>

# <editor-fold desc="Задача 18">

# user_input = input("Please enter a string: ")
#
# for i in user_input:
#     if i in string.punctuation:
#         user_input = user_input.replace(i, "")
#
# print(user_input)

# </editor-fold>

# <editor-fold desc="Задача 19">

# user_input = input("Please enter a string: ")
#
# input_length = len(user_input)
# new_string = ""
#
# if input_length % 2 != 0:
#     new_string = "".join(reversed(user_input))
#
# print(new_string)

# </editor-fold>

# <editor-fold desc="Задача 20">

# user_input = input("Please enter a digit: ")
# continue_searching = True
#
# while continue_searching:
#
#     new_pos_num = int(user_input) + 1
#     new_neg_num = int(user_input) - 1
#
#     while True:
#
#         tmp_1 = "".join(reversed(str(new_pos_num)))
#         tmp_2 = "".join(reversed(str(new_neg_num)))
#         if tmp_1 == str(new_pos_num):
#             print(f"Next palindrome number is {new_pos_num}")
#             continue_searching = False
#             break
#         else:
#             new_pos_num += 1
#
#         if tmp_2 == str(new_neg_num):
#             print(f"Next palindrome number is {new_pos_num}")
#             continue_searching = False
#             break
#         else:
#             new_neg_num += 1

# </editor-fold>

# <editor-fold desc="Задача 21">

# for i in range(0, 6):
#
#     if (i == 0) or (i == 1) or (i == 4) or (i == 5) or (i == 6):
#         print("*       *")
#     elif i == 2:
#         print("* *   * *")
#     else:
#         print("*   *   *")

# </editor-fold>

# <editor-fold desc="Задача 22">

# for i in range(0, 7):
#
#     if (i == 0) or (i == 6):
#         print("****")
#     else:
#         print("*   *")

# </editor-fold>

# <editor-fold desc="Задача 23">

# a = int(input("Please enter a number: "))
# b = int(input("Please enter a number: "))

# factorial of a

# for i in range(1, a + 1):
#     product = 1
#     for j in range(1, i + 1):
#         product *= j
#     print(product)
#
# # factorial of b
#
# for i in range(1, b + 1):
#     product = 1
#     for j in range(1, i + 1):
#         product *= j
#     print(product)
#
# print(f'result is {a / b}')

# <editor-fold desc="Задача 24">

# a = int(input("Enter a number: "))
# b = int(input("Enter a number: "))
#
# num_1 = 1
# num_2 = 1
# num_3 = 1
#
# for a in range(a+1, 1, -1):
#     num_1 *= a - 1
#
# for b in range(b+1, 1, -1):
#     num_2 *= b - 1
#
# n_k = num_1 - num_2
#
# for c in range(n_k+1, 1, -1):
#     num_3 *= c - 1
#
# calc = (num_1 * num_2) / n_k
#
# print(calc)

# </editor-fold>

# <editor-fold desc="Задача 26">

# user_input = int(input("Enter a number: "))
#
# for i in range(1, user_input+1):
#     for j in range(i, user_input+i):
#         print(j, end=" ")
#     print()

# </editor-fold>
