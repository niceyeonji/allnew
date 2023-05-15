import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt

from matplotlib import font_manager, rc
from math import sqrt

font_location = 'c:/windows/fonts/malgun.ttf'
font_name = font_manager.FontProperties(fname=font_location).get_name()
matplotlib.rc('font', family=font_name)
plt.rcParams['font.family'] = 'malgun Gothic'

theaterfile = 'theater.csv'
colnames = ['id', 'theater', 'region', 'bindo']
dftheater = pd.read_csv(theaterfile, names=colnames, header=None)
dftheater = dftheater.rename(index=dftheater.id)
dftheater = dftheater.reindex(columns=['theater', 'region', 'bindo'])
dftheater.index.name = 'id'
print('전체 조회')
print(dftheater)
print('-' * 50)

print('극장별 상영 횟수 집계')
mygrouping = dftheater.groupby('theater')['bindo']
sumSeries = mygrouping.sum()
meanSeries = mygrouping.mean()
sizeSeries = mygrouping.size()

print('시리즈별 데이터프레임 생성')
df = pd.concat([sumSeries, meanSeries, sizeSeries], axis=1)
df.columns = ['합계', '평균', '개수']
print(df)
print('-' * 50)
print(len(df))


df.plot(kind='barh', rot=0)
plt.title(str(sizeSeries) + '개 매장 집계 데이터')
filename = 'visualizationExam_01.png'
plt.savefig(filename)
print(filename + 'saved...')

print('집계 메소드를 사전에 담아 전달')
print('지역의 개수와 상영 횟수의 총합')
mydict = {'bindo' : 'sum', 'region' : 'size'}
result = dftheater.groupby('theater').agg(mydict)
print(result)
print('-' * 50)

print('numpy를 이용한 출력')
result = mygrouping.agg([np.count_nonzero, np.mean, np.std])
print(result)
print('-' * 50)

def myroot(values):
    mysum = sum(values)
    return sqrt(mysum)

def plus_add(values, somevalue):
    result = myroot(values)
    return result + somevalue

mygrouping = dftheater.groupby('theater')['bindo']
print('groupby와 사용자 정의 함수 사용')
result = mygrouping.agg(myroot)
print(result)
print('-' * 50)

print('groupby와 사용자 정의 함수(매개변수 2개) 사용')
result = mygrouping.agg(plus_add, somevalue=3)
print(result)
print('-' * 50)

print('컬럼 2개 이상을 그룹핑')
newgrouping = dftheater.groupby(['theater', 'region'])['bindo']
result = newgrouping.count()
print(result)
print('-' * 50)

newDf = df.loc[:, ['평균', '개수']]
newDf.plot(kind='bar', rot=0)
plt.title('3개 극장의 평균과 상영관 수')

filename = 'visualizationExam_02.png'
plt.savefig(filename)
print(filename + ' saved...')

lables = []
explode = (0, 0.03, 0.06)

for key in sumSeries.index:
    mydata = key + '(' + str(sumSeries[key]) + ')'
    lables.append(mydata)

fig1, ax1 = plt.subplots()
mytuple = tuple(lables)
ax1.pie(sumSeries, explode=explode, labels=mytuple, autopct='%1.1f%%', shadow=True, startangle=90)
ax1.axis('equal')
plt.show()

filename = 'visualizationExam_03.png'
plt.savefig(filename)
print(filename + ' saved...')
print('finished')