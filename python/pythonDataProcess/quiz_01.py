from bs4 import BeautifulSoup
from pandas import DataFrame
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.family'] = "Malgun Gothic"

html = open('ex5-10.html', 'r', encoding="utf-8")
soup = BeautifulSoup(html, 'html.parser')

result = []
tbody = soup.find("tbody")
tds = tbody.findAll('td')
for data in tds:
    result.append(data.text)
print(result)
print('-' * 50)

mycolumns = ['이름', '국어', '영어']

myframe = DataFrame(np.reshape(np.array(result), (4,3)),
             columns=mycolumns)
myframe = myframe.set_index(keys='이름')
print(myframe)
print('-' * 50)
# sdata = {
#     '이름' : result[::3],
#     '국어' : result[1::3],
#     '영어' : result[2::3]
# }
#
# myframe = DataFrame(sdata)
# myframe = myframe.set_index('이름')
# print(myframe)

myframe = myframe.astype(float)
myframe.plot(kind='line', title='Score', figsize=(10, 6), legend=True)
filename = 'scoreGraph.png'
plt.savefig(filename, dpi=400, bbox_inches='tight')
print(filename + ' Saved...')
plt.show()

myframe.astype(float).plot(kind='line', title='Score', legend=True)
filename='scoreGraph.png'
plt.savefig(filename, dpi=400, bbox_inches='tight')
print(filename + ' saved...')
plt.show()