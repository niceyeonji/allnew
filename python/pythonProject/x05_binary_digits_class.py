# import random
#
# class Binary_digits(object):
#
#     def __init__(self, x):
#         self.x = x
#
#     def binary_digits(self):
#         if self.x // 2 == 0:
#             return str(self.x % 2)
#         return Binary_digits(self.x // 2).binary_digits() + str(self.x % 2)
#
#
# n = random.sample(range(4, 16), 1)[0]
# binary_convert = Binary_digits(n)
# binary_digits = binary_convert.binary_digits()
# print(f'{n} binary_digits is: {binary_digits}')

import random

class Binary_digits(object):

    def __init__(self, x):
        self.x = x

    def covert(self):
        digits = []
        while self.x > 0:
            digits.append(self.x % 2)
            self.x = self.x // 2
        return digits[::-1]

n = random.randrange(4, 16)
binary_covert = Binary_digits(n)
print(f'{n} binary number is: {binary_covert.covert()}')


# 희연
# import random
#
# class Binary_digits(object):
#     def __init__(self,d):
#         self.d=d
#     def covert(self):
#         binary = []
#         while (self.d * 2) // 2 > 0:
#             r = self.d % 2
#             binary.append(r)
#             self.d = self.d // 2
#         return (list(reversed(binary)))
#
# d=random.randrange(4,16)
# result=Binary_digits(d)
# print(f'Binary of {d} = {result.covert()}')


# 교수님
# import random
#
# class Binary_digits(object):
#     def __init__(self, num, lists):
#         self.num = num
#         self.lists = lists
#     def convert(self):
#         q = self.num
#         lists = self.lists
#         while True:
#             r = q % 2
#             q = q // 2
#             lists.append(r)
#             if q == 0:
#                 break
#         lists.reverse()
#         return lists
#
# lists = []
# num = random.randrange(4, 16)
# binary = Binary_digits(num, lists)
# print(f'{num} binary number is : {binary.convert()}')