# def divide(a, b):
#     return (a / b, a % b)
#
# a = int(input("Input first number : "))
# b = int(input("Input Second number : "))
#
# print("Input number {} / {}".format(a, b))
# q, r = divide(int(a), int(b))
# print("quotient : {}".format(int(q)))
# print("Remainder : {}".format(r))

def divide(a, b):
    return (a / b, a % b)

a = input("Input first number : ")
b = input("Input Second number : ")

print(f"Input number {a} / {b}")
q, r = divide(int(a), int(b))
print("Quotient : ", int(q))
print("Remainder : ", r)