import os

myfolder = './'
newpath = os.path.join(myfolder, 'work')

try:
    os.mkdir(path=newpath)

    for idx in range(1, 11):
        newfile = os.path.join(newpath, 'somefolder' + str(idx).zfill(2))
        # zfill(2)은 2자리로 채우라는 뜻. 폴더이름을 보면 01, 02 이런식으로 되어있음.
        os.mkdir(path=newfile)
except FileExistsError:
    print('Directory exist already...')
print('finished')
