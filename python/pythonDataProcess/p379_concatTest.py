import pandas as pd

afile = 'android.csv'
bfile = 'iphone.csv'

atable = pd.read_csv(afile, encoding='utf-8')
btable = pd.read_csv(bfile, encoding='utf-8')

print(atable)
print('-' * 50)
print(btable)
print('-' * 50)

atable['phone']='안드로이드'
btable['phone']='아이폰'

mylist = []
mylist.append(atable)
mylist.append(btable)
result = pd.concat(objs=mylist, axis=0, ignore_index=True)
print(result)
filename = 'result.csv'
result.to_csv(filename, encoding='utf-8')
print(filename+' saved...')