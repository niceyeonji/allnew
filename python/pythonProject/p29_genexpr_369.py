# numbers = (i for i in range(1, 101))
#
# print(list(numbers))

# def game369(num):
#     str_num = str(num)
#     if '33' in str_num or '36' in str_num or '39' in str_num or '63' in str_num or '66' in str_num or '69' in str_num or '93' in str_num or '96' in str_num or '99' in str_num:
#         return '👏👏'
#     elif '3' in str_num or '6' in str_num or '9' in str_num:
#         return '👏'
#     else:
#         return num
#
# # numbers = (i for i in range(1, 101))
# # result = [game369(num) for num in numbers]
# # print(result)
#
# numbers = (i for i in range(1, 101))
# for num in numbers:
#     print(game369(num))
#
def game369(num):
    count = str(num).count('3') + str(num).count('6') + str(num).count('9')
    if count == 1:
        return '👏'
    elif count == 2:
        return '👏👏'
    else:
        return num

numbers = (i for i in range(1, 101))
for num in numbers:
    print(game369(num))

print("----------------------------------------")

numbers = (i for i in range(1,101))

data = list(numbers)

item = [3, 6, 9]

for i in data:
    n10 = int(i/10)
    n1 = i %10
    if i % 10 == 1:
        print()
    if i < 10:
        if i in item:
            print(' 👏', end="")
        else:
            print("%4d" % i, end="")
    else:
        if n10 in item and n1 in item:
            print(' 👏👏', end="")
        elif n10 in item or n1 in item:
            print(' 👏', end="")
        else:
            print("%4d" % i, end="")