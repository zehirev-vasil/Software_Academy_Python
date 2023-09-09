# <editor-fold desc="Задача 1">

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

numbers = []
while len(numbers) < 4:
    try:
        numbers = input("Въведете списък от числа: ").split(",")
        numbers = [int(number) for number in numbers]
    except ValueError:
        print("Невалиден списък от числа.")

# Премахване на най-крайните стойности.
new_numbers = []
for number in numbers:
    if str(number) not in str(min(numbers)) and str(number) not in str(max(numbers)):
        new_numbers.append(number)


# Отпечатване на оригиналния и новия списък.
print("Оригинален списък:", numbers)
print("Нов списък:", new_numbers)


# my_list = []
