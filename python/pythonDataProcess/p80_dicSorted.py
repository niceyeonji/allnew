wordInfo = {'세탁기' : 50, '선풍기' : 30, '청소기' : 40, '냉장고' : 60}

myxticks = sorted(wordInfo, key=wordInfo.get, reverse=True)
print(myxticks)

revers_key = sorted(wordInfo.keys(), reverse=True)
print(revers_key)

chartdata = sorted(wordInfo.values(), reverse=True)
print(chartdata)