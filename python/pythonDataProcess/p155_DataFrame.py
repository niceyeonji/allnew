from pandas import DataFrame

sdata = {
    '도시' : ['서울', '서울', '서울', '부산', '부산'],
    '연도' : [2000, 2001, 2002, 2001, 2002],
    '실적' : [150, 170, 360, 240, 290]

}

myindex = ['one', 'two', 'three', 'four', 'five']
myframe = DataFrame(sdata, index=myindex)
print('\nType : ', type(myframe))

myframe.columns.name = 'Columns1'
print('\nColumns Information')
print(myframe.columns)

myframe.index.name = 'Index1'
print('\nIndex Information')
print(myframe.index)

print('\nInner data Information')
print(type(myframe.values))
print(myframe.values)

print('\nInner Type Information')
print(myframe.dtypes)

print('\nContext Information')
print(myframe)

print('\nrow, col transform')
print(myframe.T)

print('\ncolumns property usage')
mycolumns = ['연도', '도시', '실적']
newframe = DataFrame(sdata, columns=mycolumns)
print(newframe)
