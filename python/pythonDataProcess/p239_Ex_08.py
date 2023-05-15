import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['font.family'] = 'Malgun Gothic'

filename = 'tips.csv'

myframe = pd.read_csv(filename, encoding='utf-8')
print('head() 메소드 결과')
print(myframe.head())
print('-' * 40)

print('info() 메소드 결과')
print(myframe.info())
print('-' * 40)

mycolors = ['r', 'b']
labels = ['Female', 'Male']
print(labels)

cnt = 0

for finditem in labels:
    xdata = myframe.loc[myframe['sex'] == finditem, 'total_bill']
    ydata = myframe.loc[myframe['sex'] == finditem, 'tip']
    plt.plot(xdata, ydata, color=mycolors[cnt], marker='o', linestyle='None', label=finditem)
    cnt += 1

plt.legend(loc=4)
plt.xlabel("결재 총액")
plt.ylabel("팁 비용")
plt.title("결재 총액과 팁 비용의 산점도")
plt.grid(True)

filename = 'dataframeGraph02_06.png'
plt.savefig(filename, dpi=400, bbox_inches='tight')
print(filename + ' Saved...')
print('-' * 40)

plt.show()
