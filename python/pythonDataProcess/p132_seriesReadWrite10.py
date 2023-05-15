from pandas import Series

myindex = ['용산구', '마포구', '영등포구', '서대문구', '광진구', '은평구','서초구']

mylist = [50, 60, 40, 80, 70, 30, 20]

myseries = Series(data=mylist, index=myindex)
print(myseries)

print('\nread value')
print(myseries[['서대문구']])

print('\nslicing label name')
print(myseries['서대문구':'은평구'])

print('\ndata read')
print(myseries[['서대문구','서초구']])

print('\nread index')
print(myseries[[2]])

print('\nread index 0, 2, 4')
print(myseries[0:5:2])

print('\nread index 1, 3, 5')
print(myseries[[1,3,5]])

print('\nslicing')
print(myseries[3:6])

myseries[2]=90
myseries[2:5] = 33
myseries[['용산구', '서대문구']] = 55
myseries[0::2] = 80
print(myseries)