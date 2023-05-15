import pandas as pd
import urllib.request
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
from pandas import DataFrame

plt.rcParams['font.family'] = 'Malgun Gothic'

myurl = 'https://movie.daum.net/ranking/reservation'
html = urllib.request.urlopen(myurl)
soup = BeautifulSoup(html, 'html.parser')

mytargets = soup.findAll('div', attrs={'class':'thumb_cont'})
# print(mytargets)

no = 0
myframe = pd.DataFrame()

for target in mytargets:
    result = []
    no += 1

    mytitle = target.find('a', attrs={'class':'link_txt'})
    title = mytitle.string
    # print('제목 : ' + title)

    myscore = target.find('span', attrs={'class':'txt_grade'})
    score = myscore.string
    # print('평점 : ' + score)

    mybooked = target.find('span', attrs={'class':'txt_num'})
    booked = mybooked.string.replace('%', '')
    # print('예매율 : ' + booked)

    mydata = target.find('span', attrs={'class': 'txt_info'})
    mydata2 = mydata.find('span', attrs={'class': 'txt_num'})
    target = mydata2.string
    # print('-' * 50)

    # result.append([no, title, score, booked, target])
    result.append([title, score, booked])
    myframe = pd.concat([myframe, pd.DataFrame(result)], axis=0)

# myframe.columns = ['순위', '제목', '평점', '예매율', '개봉일']
# myframe.set_index("순위", inplace=True)
myframe.columns = ['제목', '평점', '예매율']
myframe.set_index("제목", inplace=True)

myframe.astype(float).plot(kind='barh', title='영화별 평점과 예매율', figsize=(10, 6), legend=True)
plt.show()

print(myframe)
print(myframe.info())