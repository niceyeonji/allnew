import pandas as pd

result =[]
myColumns = ('이름', '나이')
myencoding = 'utf-8'
mydata = [('김철수', 10), ('박영희', 20)]

for idx in mydata :
    name = idx[0]
    age = idx[1]

    sublist = []
    sublist.append(name)
    sublist.append(age)
    result.append(sublist)

myframe = pd.DataFrame(result, columns=myColumns)

filename = 'csv_02_01.csv'
myframe.to_csv(filename, encoding=myencoding, mode='w', index=False)

filename = 'csv_02_02.csv'
myframe.to_csv(filename, encoding=myencoding, mode='w', index=False, sep='#')

print(filename + ' 파일 저장 완료')