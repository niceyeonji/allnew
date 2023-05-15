import urllib.request
import pandas as pd
from bs4 import BeautifulSoup
from pandas import DataFrame
import matplotlib.pyplot as plt

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
####################################################################################################
plt.rcParams['font.family'] = 'Malgun Gothic'
myframe = pd.read_csv(filename, index_col='제목', encoding='utf-8')
myframe.index.name = '제목'
myframe['예매율'] = myframe['예매율'].str.strip('%').astype(float)
myframe[['평점', '예매율']].plot(kind='barh',color=['r', 'b'], rot=0, title='평점과 예매율')

filename = 'bs4_exam.png'
plt.savefig(filename, dpi=400, bbox_inches='tight')
print(filename + ' Saved…')
print('-' * 100)
plt.show()