import p25_timer

timer = p25_timer.counter2()
counter = 0
sum = 0
while True:
    sum += 7
    if sum > 100:
        break
    counter = timer()
print(f'result : {counter}')