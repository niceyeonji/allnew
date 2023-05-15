import urllib.request

url = "https://shared-comic.pstatic.net/thumb/webtoon/626907/thumbnail/title_thumbnail_20150407141027_t83x90.jpg"
savename = 'urldownload01.png'

urllib.request.urlretrieve(url, savename)

print('web image : ' + url)
print(savename + 'saved...')