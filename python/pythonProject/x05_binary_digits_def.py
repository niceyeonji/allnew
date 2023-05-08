# import random
#
# def binary_digits(x):
#     if x // 2 == 0:
#         return x % 2
#     return binary_digits(x // 2) + str(x % 2)
#
# n = random.sample(range(4, 17), 1)[0]
# print(f'{n} binary_digits is : {binary_digits(n)}')

import random
def binary_digits(x):
    digits = []
    while x > 0:
        digits.append(x % 2)
        x = x // 2
    return digits[::-1]

# n = random.sample(range(4, 16), 1)[0]
n = random.randrange(4, 16)
print(f'{n} binary number is : {binary_digits(n)}')

import random




