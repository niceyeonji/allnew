from pandas import Series

mylist = [200, 300, 400, 100]
myseries = Series(data=mylist, index=['손오공', '저팔계', '사오정', '삼장법사'])

myseries.index.name = '실적 현황'
print('\n# 시리즈의 색인 이름')
print(myseries.index.name)

myseries.name = '직원 실적'
print('\n# 시리즈의 이름')
print(myseries.name)

print('\n# 반복하여 출력해보기')
for idx in myseries.index:
    print('색인 : ' + idx + ', 값 : ' + str(myseries[idx]))