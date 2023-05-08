while True:
    a = input("Input number range 2~9!! (q: Quit) : ")
    if a == 'q':
        print("Exit")
        break
    else:
        if int(a) < 2 or int(a) > 9:
            print("input number range 2~9!!")
        else:
            for i in range(1, 10):
                print(a, "*", i, "=", int(a) * i)


# while True:
#     n = input("Input number (q: Quit) : ")
#     if n == 'q':
#         print("Exit")
#         break
#     n = int(n)
#     if (n < 2 or n > 9):
#         print("input number range 2~9!!")
#         continue;
#     else:
#         for c in range(1, 10):
#             print(f'{n} * {c} = {n * c}')