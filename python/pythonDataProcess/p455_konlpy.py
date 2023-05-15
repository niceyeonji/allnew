from konlpy.tag import Komoran

sentence = '코로나 바이러스 태블릿 PC, 설진욱, 가나다라'
print('# before user dic')
komo = Komoran()
print(komo.pos(sentence))
print('-' * 40)

komo = Komoran(userdic='user_dic.txt')
print('# after user dic')
print(komo.pos(sentence))
print('-' * 40)

print('# komo.nouns')
result = komo.nouns(sentence)
print(result)
print('-' * 40)

print('# komo.morphs')
result = komo.morphs(sentence)
print(result)
print('-' * 40)
