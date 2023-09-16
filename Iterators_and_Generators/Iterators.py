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
