# mynum 리스트의 항목을 꺼내서 제곱값을 출력하는 제너레이터 함수

def square_number(nums):
# square_number()는 nums인자로 리스트를 받음
    for t in nums:
# for 반복문을 이용해 리스트의 각 항목값을 꺼냄
        yield t ** 2
# 제곱값을 계산해 yield로 반환함. 이렇게 제너레이터 함수 생성!

mynum = [1, 2, 3, 4, 5]

for square in square_number(mynum):
# for 반복문에서 제너레이터 객체를 이용해 각 항목의 제곱값 출력
    print(square)

# def square_number(nums):
#     for i in nums:
#         yield i * i
# mynum = [1, 2, 3, 4, 5]
# result = square_number(mynum)
#
# for i in range(len(mynum)):
#     print(f'Square value of mynum[{i}] = {mynum[i]} : {next(result)}')