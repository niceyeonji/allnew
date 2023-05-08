import calc_func

a = int(input("Input first number : "))
b = int(input("Input second number : "))

print('{} + {} = {}'.format(a, b, calc_func.add(a, b)))
print('{} + {} = {}'.format(a, b, calc_func.sub(a, b)))
