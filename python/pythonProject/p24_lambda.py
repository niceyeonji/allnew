i = input("Input first number : ")
j = input("Input second number : ")

a = lambda i, j : i + j
print('{} + {} = {}'.format(i , j, a(int(i), int(j))))