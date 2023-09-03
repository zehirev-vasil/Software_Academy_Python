# <editor-fold desc="Задача 1">
# for i in range(1500, 2700):
#     if i % 7 == 0 and i % 5 == 0:
#         print(i)
# </editor-fold>

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
