# def gcd(a, b):
#     while b != 0:
#         a, b = b, a % b
#     return a
#
# a = int(input("Input First number : "))
# b = int(input("Input Second number : "))
# print(f'gcd({a}, {b}) of {a}, {b} : {gcd(a, b)}')
#

def gcd(a, b):
    print("gcd", (a, b))
    while b != 0:
        r = a % b
        a = b
        b = r
        print("gcd", (a, b))
    return a

a = int(input("Input First number : "))
b = int(input("Input Second number : "))
print(f'gcd({a}, {b}) of {a}, {b} : {gcd(a, b)}')