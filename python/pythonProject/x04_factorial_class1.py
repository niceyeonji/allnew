# class Factorial(object):
#     def __init__(self):
#         pass
#     def factorial(self, x):
#         if x == 0:
#             return 1
#         else:
#             return x * self.factorial(x - 1)
#
# a = int(input("Input First number : "))
# factorial1 = Factorial()
# print(f'{a} factorial = {factorial1.factorial(a)}')


class Factorial(object):
    def __init__(self, x):
        self.x = x
    def factorial(self):
        if self.x == 0:
            return 1
        n = self.x
        self.x -= 1
        return n * self.factorial()

input = int(input("Input First number : "))
fact = Factorial(input)
print(f'{input} factorial = {fact.factorial()}')

# class Factorial(object):
#     def __init__(self, x):
#         self.x = x
#     def factorial(self):
#         if self.x == 0:
#             return 1
#         else:
#             return self.x * Factorial(self.x - 1).factorial()
#
# input = int(input("Input the number : "))
# print(f'{input} Factorial.factorial = {Factorial(input).factorial()}')