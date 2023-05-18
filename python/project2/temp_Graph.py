import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.family'] = "AppleGothic"

filename = 'temp.csv'
myframe = pd.read_csv(filename, encoding='utf-8')

myframe = myframe.set_index(keys='년월')
print(myframe)

myframe.plot(kind='line', title='여름 평균기온', figsize=(10, 6), legend=True)

filename = 'temp_Graph.png'
plt.savefig(filename, dpi=400, bbox_inches='tight')
print(filename + ' Saved...')
plt.show()