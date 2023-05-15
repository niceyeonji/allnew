import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.family'] = 'Malgun Gothic'

filename = 'daumMovie.csv'

myframe = pd.read_csv(filename, index_col='제목', encoding='utf-8')
# myframe['평점'] = myframe['평점']
# myframe['예매율'] = myframe['예매율']

#GPT 빌린부분
myframe['평점'] = myframe['평점'].astype(float)
myframe['예매율'] = myframe['예매율'].str.replace('%', '').astype(float)

myframe[['평점', '예매율']].plot(kind='barh', rot=0, title='영화별 평점과 예매율', legend=True)
print(myframe)
print('-' * 40)

filename = 'a.png'
plt.savefig(filename, dpi=400, bbox_inches='tight')
print(filename + 'Saved...')
plt.show()