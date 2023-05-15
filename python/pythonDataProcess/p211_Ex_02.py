from pandas import DataFrame as df
import numpy as np

# sdata = {
#     '국어' : [60.00, np.nan, 40.00],
#     '영어' : [np.nan, 80.00, 50.00],
#     '수학' : [90.00, 50.00, np.nan]
# }

mydata = [[60.00, np.nan, 90.00], [np.nan, 80.00, 50.00], [40.00, 50.00, np.nan]]
myindex = ['강감찬', '김유신', '이순신']
mycolumn = ['국어', '영어', '수학']
myframe = df(data=mydata, index=myindex, columns=mycolumn)

# myframe = df(data=sdata, index=['강감찬', '김유신', '이순신'])
print('# Before')
print(myframe)

# myframe.loc[['강감찬'], ['영어']] = 65.00
# myframe.loc[['김유신'], ['국어']] = 50.00
# myframe.loc[['이순신'], ['수학']] = 70.00

myframe.loc[myframe['국어'].isnull(), '국어'] = myframe['국어'].mean()
myframe.loc[myframe['영어'].isnull(), '영어'] = myframe['영어'].mean()
myframe.loc[myframe['수학'].isnull(), '수학'] = myframe['수학'].mean()

print('\n# After')
print(myframe)
print('-' * 40)
print(myframe.describe())
