import numpy as np
from pandas import Series, DataFrame

myindex = ['강호민', '유재준', '신동진']
mylist = [30, 40, 50]

myseries = Series(data=mylist, index=myindex)
print('\nseries print')
print(myseries)

myindex = ['강호민', '유재준', '이수진']
mycolumns = ['서울', '부산', '경주']
mylist = list(10 * onedata for onedata in range(1, 10))

myframe = DataFrame(np.reshape(np.array(mylist), (3, 3)), index=myindex, columns=mycolumns)
print('\nDataFrame print')
print(myframe)

print('\nDataFrame + Series')
# 연산을 하기 위해서 axis = 0을 쓴다. axis =0은 행방향, axis=1은 열방향
result = myframe.add(myseries, axis = 0)
print(result)

myindex2 = ['강호민', '유재준', '김병준']
mycolumns2 = ['서울', '부산', '대구']
mylist2 = list(5 * onedata for onedata in range(1, 10))

myframe2 = DataFrame(np.reshape(np.array(mylist2), (3, 3)),
                     index=myindex2, columns=mycolumns2)
print('\nDataFrame + DataFrame')
result = myframe.add(myframe2, fill_value = 0)
print(result)