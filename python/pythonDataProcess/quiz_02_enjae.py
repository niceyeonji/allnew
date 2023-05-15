import urllib.request
from bs4 import BeautifulSoup
import pandas as pd
from pandas import DataFrame
import matplotlib.pyplot as plt

plt.rcParams['font.family'] = 'Malgun Gothic'

url = "https://movie.daum.net/ranking/reservation"
html = urllib.request.urlopen(url)
soup = BeautifulSoup(html, 'html.parser')

infos = soup.findAll('div', attrs={'class':'thumb_cont'})

# print('-' * 40)
# print(infos)
# print('-' * 40)

no = 0
result = []
for info in infos:
    no += 1
    mytitle = info.find('a', attrs={'class':'link_txt'})
    title = mytitle.string

    mygrade = info.find('span', attrs={'class':'txt_grade'})
    grade = mygrade.string

    mynum = info.find('span', attrs={'class':'txt_num'})
    num = mynum.string

    myrelease = info.find('span', attrs={'class':'txt_info'})
    release = myrelease.span.string

    result.append((no, title, grade, num, release))
# print(result)

print('-' * 40)

mycolumn = ['순위', '제목', '평점', '예매율', '개봉일']

myframe = DataFrame(result, columns=mycolumn)
newdf = myframe.set_index(keys=['순위'])
print(newdf)
print('-' * 40)

filename = 'daumMovie.csv'
myframe.to_csv(filename, encoding='utf8', index=False)
print(filename, ' saved...', sep='')
print('finished')

dfmovie = myframe.reindex(columns=['제목', '평점', '예매율'])
print(dfmovie)

mygroup0 = dfmovie['제목']
mygroup1 = dfmovie['평점']
mygroup2 = dfmovie['예매율']
mygroup2 = mygroup2.str.replace('%','')

df = pd.concat([mygroup1, mygroup2], axis=1)
df = df.set_index(mygroup0)
df.columns = ['평점', '예매율']
print(df)

df.astype(float).plot(kind='barh', title='영화별 평점과 예매율', rot=0)
filename = 'daumMovieGraph.png'
plt.savefig(filename, dpi=400, bbox_inches='tight')
plt.show()