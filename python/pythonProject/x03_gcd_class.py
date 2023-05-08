# class Gcd(object):
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#     def gcd(self):
#         while self.b != 0:
#             self.a, self.b = self.b, self.a % self.b
#             print("gcd", (self.a, self.b))
#         return self.a
#
#
# a = int(input("Input First number : "))
# b = int(input("Input Second number : "))
# gcd1 = Gcd(a ,b)
# print(f'gcd({a}, {b}) of {a}, {b} : {gcd1.gcd()}')

class Gcd(object):
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def gcd(self):
        print("gcd", (self.a, self.b))
        while self.b != 0:
            self.r = self.a % self.b
            self.a = self.b
            self.b = self.r
            print("gcd", (self.a, self.b))
        return self.a

a = int(input("Input First number : "))
b = int(input("Input Second number : "))

gcd1 = Gcd(a, b)
print(f'gcd({a}, {b}) of {a}, {b} : {gcd1.gcd()}')