# def prime(a):
#     for i in range(2, a):
#     	if a % i == 0:
#         	return 0
#     return 1


def prime(a):
    for k in (2, a):
        if a % k == 0:
            break
    if k == a:
        return 1
    else:
        return 0