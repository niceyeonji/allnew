from pandas import Series

print('\nUnique, count, isin')
mylist = ['라일락', '코스모스', '코스모스', '백일홍', '코스모스', '코스모스', '들장미', '들장미', '라일락', '라일락']
myseries = Series(mylist)

print('\nUnique()')
myunique = myseries.unique()
print(myunique)

print('\nvalue_count()')
print(myseries.value_counts())

print('\nisin()')
mask = myseries.isin(['들장미', '라일락'])
print(mask)
print('-' * 50)

print(myseries[mask])
print('-' * 50)

print('\nfinished')