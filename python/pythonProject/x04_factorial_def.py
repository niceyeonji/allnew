## fibonaci
## f(x) = 1, x = 0
## f(x) = f(x-1)*x, x>1

def factorial(x):
    if x == 0:
        return 1
    else :
        return x * factorial(x - 1)

input = int(input("Input the number : "))
print(f'{input} factorial = {factorial(input)}')

