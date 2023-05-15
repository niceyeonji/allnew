import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.family'] = 'Malgun Gothic'

chickenfile = 'chicken.csv'
colnames = ['지역', '브랜드', '매장수']
myframe = pd.read_csv(chickenfile, names=colnames, header=None)
print(myframe)
print('-' * 40)

mygrouping = myframe.groupby('브랜드')['매장수']
meanSeries = mygrouping.sum()
meanSeries.index.name = '브랜드'
print(meanSeries)
print('-' * 40)

mycolor = ['red', 'green', 'blue']
mytitle = '브랜드별 매장 개수'
myylim = [0, meanSeries.max() + 5]
myalpha = 0.7

meanSeries.plot(kind='bar', color=mycolor, title=mytitle, legend=False, rot=15, ylim=myylim, grid=False, alpha=myalpha)

filename = 'xx_chick.png'
plt.savefig(filename, dpi=400, bbox_inches='tight')
plt.show()

print('finished.')
