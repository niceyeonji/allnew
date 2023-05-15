import re

mylist = ['ab123', 'cd4#6', 'cf79a', 'abc1']

regex = '[ac]{1}\w{4}'
pattern = re.compile(regex)

print('# 문자 a 또는 c로 시작하고, 이후 숫자 또는 알파벳이 4개로 끝나는 항목')
totallist = []
for item in mylist:
    if pattern.match(item):
        print(item, '은(는) 조건에 적합')
        totallist.append(item)
    else:
        print(item, '은(는) 조건에 부적합')
print('\n적합한 항목들')
print(totallist)