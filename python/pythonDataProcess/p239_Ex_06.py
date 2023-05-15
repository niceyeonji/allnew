from pandas import Series
import matplotlib.pyplot as plt

plt.rc('font', family='Malgun Gothic')

myindex = ['강감찬', '김유신', '이순신', '안익태', '윤동주']
member = Series(data=[30, 20, 40, 30, 60], index=myindex)
print(member)
print('-' * 50)

member.plot(kind='bar', rot=0, ylim=[0, member.max() + 4], use_index=True, grid=False, table=False, color=['r', 'g', 'b', 'y', 'm'])
plt.xlabel('학생 이름')
plt.ylabel('점수')
plt.title('학생별 시험 점수')

ratio = 100 * member / member.sum()
print(ratio)
print('-' * 50)

for idx in range(member.size):
    value = str(member[idx]) + '건'
    ratioval = '%.1f%%' % (ratio[idx])

    plt.text(x=idx, y=member[idx] + 1, s=value, horizontalalignment='center')
    plt.text(x=idx, y=member[idx] / 2, s=ratioval, horizontalalignment='center')

meanval = member.mean()
print(meanval)
print('-' * 50)

average = '평균 : %d건' % meanval
plt.axhline(y=meanval, color='r', linewidth=1, linestyle='dashed')
plt.text(x=0, y=meanval + 1, s=average, horizontalalignment='center')

filename = 'graph02.png'
plt.savefig(filename, dpi=400, bbox_inches='tight')
print(filename + ' Saved...')
plt.show()