import matplotlib.pyplot as plt
plt.rcParams['font.family'] = 'malgun Gothic'

slices = [1, 2, 3, 4]
hobbies = ['잠자기', '외식', '영화 감상', '운동']
mycolors = ['blue', '#6AFF00', 'yellow', '#FF003C']

plt.pie(x=slices, labels=hobbies, shadow=True, explode=(0, 0.1, 0, 0),
        colors=mycolors, autopct='%1.2f%%', startangle=90, counterclock=False)

plt.legend(loc=4)

filename = 'pieGraph01.png'
plt.savefig(filename, dpi=400, bbox_inches='tight')
print(filename + ' Saved...')
plt.show()