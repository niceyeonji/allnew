import pandas as pd

afile = 'data03.csv'
bfile = 'data04.csv'

atable = pd.read_csv(afile, header=0, encoding='utf-8')
btable = pd.read_csv(bfile, header=None, encoding='utf-8', names=['이름','성별','국어','영어','수학'])

print(atable)
print('-' * 40)
print(btable)
print('-' * 40)

atable['반'] = '1반'
btable['반'] = '2반'

mylist = []
mylist.append(atable)
mylist.append(btable)

result = pd.concat(objs=mylist, axis=0, ignore_index=True)
print(result)
print('-' * 40)

dropIndex = result[result['이름'] == '심형식'].index
print(dropIndex)
print('-' * 40)

newResult = result.drop(dropIndex)
print(newResult)
print('-' * 40)

filename = 'result.csv'
newResult.to_csv(filename, encoding='utf-8')
print(filename + ' saved...')