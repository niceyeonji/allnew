import pandas as pd
from pandas import DataFrame

dict1 = {'name':['김유신', '김유신', '이순신', '박영효', '이순신', '이순신', '김유신'], 'korean': [60, 50, 40, 80, 30, 55, 45]}
df1 = DataFrame(dict1)

dict2 = {'name':['이순신', '김유신', '신사임당'], 'english':[60, 55, 80]}
df2 = DataFrame(dict2)

print('\n# DataFrame 출력 01')
print(df1)

print('\n# DataFrame 출력 02')
print(df2)

print('\n# merge() 메소드의 on="name"을 이용하여 데이터 합치기')
print(pd.merge(df1, df2, on='name'))
print('\n# merge() 메소드의 how="outer"을 이용하여 데이터 합치기')
print(pd.merge(df1, df2, how='outer'))