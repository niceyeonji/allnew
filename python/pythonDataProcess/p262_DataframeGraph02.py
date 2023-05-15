import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.family'] = 'Malgun Gothic'

filename = 'ex802.csv'

myframe = pd.read_csv(filename, index_col='type', encoding='utf-8')
myframe.index.name = '자동차 유형'
myframe.columns.name = '도시(city)'

myframe.plot(kind='bar', rot=0, title='지역별 차량 등록 대수', legend=True)

print(myframe)
print('-' * 40)

filename = 'dataframeGraph02_01.png'
plt.savefig(filename, dpi=400, bbox_inches='tight')
print(filename + ' Saved...')

myframeT = myframe.T
print(myframeT)
print('-' * 40)

myframeT.plot(kind='bar', rot=0, title='지역별 차량 등록 대수', legend=True)
filename = 'dataframeGraph02_02.png'
plt.savefig(filename, dpi=400, bbox_inches='tight')
print(filename + ' Saved…')
print('-' * 40)

ymax = myframeT.sum(axis=1)
ymaxlimit = ymax.max() + 10

myframeT.plot(kind='bar', ylim=[0, ymaxlimit], rot=0, stacked=True, title='지역별 차량 등록 대수', legend=True)
filename = 'dataframeGraph02_03.png'
plt.savefig(filename, dpi=400, bbox_inches='tight')
print(filename + ' Saved…')
plt.show()
