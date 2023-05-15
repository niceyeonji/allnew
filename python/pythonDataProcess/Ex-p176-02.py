from pandas import Series

myindex = ['강감찬', '이순신', '김유신', '광해군', '연산군', '을지문덕']
mylist = [50, 60, 40, 80, 70, 20]
myseries = Series(data=mylist, index=myindex)
print(myseries)

print('\n1번째 항목을 100으로 변경')
myseries[1] = 100

print('\n2번째 ~ 4번째 항목을 999로 변경')
myseries[2:5] = 999

print('\n강감찬과 을지문덕을 30으로 변경')
myseries[['강감찬', '을지문덕']] = 30

print('\n시리즈 내용 확인')
print(myseries)