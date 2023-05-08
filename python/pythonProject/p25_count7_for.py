import p25_timer

# def counter7():
#     t = [7, 100]
#     def increment():
#         t[0] += 7
#         return t[100 % 7 == 0]
#     return increment
#
# timer = counter7()
# print(timer())

# timer = p25_timer.counter2()
# for i in range(1,101):
#     if i % 7 == 0:
#         print(timer())


# def count7():
#     count = p25_timer.counter2()
#     result = 0
#     for i in range(1, 101):
#         if i % 7 == 0:
#             result = count()
#     return result
#
# print(count7())

timer = p25_timer.counter2()
counter = 0

for k in range(1,101):
    if k % 7 == 0:
        counter = timer()
print(f'result : {counter}')