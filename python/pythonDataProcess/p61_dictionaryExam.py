dictionary = {'김유신' : 50, '윤봉길' : 40, '김구' : 60}
print('ditionary list : ', dictionary)

for key in dictionary.keys():
    print(key)

for value in dictionary.values():
    print(value)

for key in dictionary.keys():
    print('{}의 나이는 {}입니다.'.format(key, dictionary[key]))

for key, value in dictionary.items():
    print('{}의 나이는 {}입니다'.format(key, value))

findKey = '유관순'

if findKey in dictionary:
    print(findKey + '(은)는 존재합니다.')
else:
    print(findKey + '(은)는 존재하지 않습니다.')

result = dictionary.pop('김구')
print('After pop dictionary : ', dictionary)
print('pop value : ', result)

dictionary.clear()
print('dictionary list : ', dictionary)