# import prime_func
#
# a = int(input("Input number : "))
#
# if prime_func.prime(a) == 0:
#     print('{} is not prime number'.format(a))
# else:
#     print('{} is prime number'.format(a))

import prime_func
while True:
    a = int(input("Input number (0 : Quit) : "))
    if (a == 0):
        break
    if (a < 2):
        print("re-enter number~!!")
        continue
    print(f"{a} is prime number") if prime_func.prime(a) == 1 else print(f"{a} is not prime number")