import urllib.request

url = "https://shared-comic.pstatic.net/thumb/webtoon/626907/thumbnail/title_thumbnail_20150407141027_t83x90.jpg"

savename = 'urldownload02.png'

result = urllib.request.urlopen(url)

data = result.read()
print('# type(data) : ', type(data))

with open(savename, mode='wb') as f:
    f.write(data)
    print(savename + ' save...')

