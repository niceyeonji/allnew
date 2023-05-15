tuple01 = (10, 20, 30)
tuple01 = tuple01 + (40, )

print('print Tuple : ', tuple01)

# tuple은 원래 값을 못바꾸는데, 위 방법을 쓰면 바꿀 수 있음!

tuple02 = 10, 20, 30, 40

mylist = [10, 20, 30, 40]
tuple03 = tuple(mylist)

if tuple02 == tuple03:
    print("Component equal")
else:
    print("Component not equal")

tuple04 = (10, 20, 30)
tuple05 = (40, 50, 60)
tuple06 = tuple04 + tuple05
print(tuple06)

tuple07 = tuple04 * 3
print(tuple07)

a, b = (11, 22)
a, b = b, a

print('a =', a, 'b =', b)

tuple08 = (11, 22, 33, 44, 55, 66)
print(tuple08[1:3])
print(tuple08[3:])