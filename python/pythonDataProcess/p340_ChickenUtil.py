import time, datetime, ssl
import pandas as pd
import urllib.request

from selenium import webdriver
from selenium.webdriver.common.by import By

from bs4 import BeautifulSoup

class ChickenStore():
    myencoding = 'utf-8'

    def getWebDriver(self, cmdJavaScript):
        # cmdJavaScript : 문자열로 구성된 자바 스크립트 커맨드
        print(cmdJavaScript)
        self.driver.execute_script(cmdJavaScript)
        wait = 5
        # self.driver.implicitly_wait(wait)
        time.sleep(wait)
        mypage = self.driver.page_source

        return BeautifulSoup(mypage, 'html.parser')

    def getSoup(self):
        if self.soup == None:
            return None
        else:
            if self.brandName != 'pelicana':
                return BeautifulSoup(self.soup, 'html.parser')
            else:  # 페리카나 # Some characters could not be decoded, and were replaced with REPLACEMENT CHARACTER.
                return BeautifulSoup(self.soup, 'html.parser')
                # return BeautifulSoup(self.soup, 'html.parser', from_encoding="iso-8859-1")

    def get_request_url(self):
        request = urllib.request.Request(self.url)
        try:
            context = ssl._create_unverified_context()
            response = urllib.request.urlopen(request, context=context)
            if response.getcode() == 200:
                # print('[%s] url request success' % datetime.datetime.now())

                if self.brandName != 'pelicana':
                    return response.read().decode(self.myencoding)
                else:
                    return response

        except Exception as err:
            print(err)
            now = datetime.datetime.now()
            msg = '[%s] error for url %s' % (now, self.url)
            print(msg)
            return None

    def save2Csv(self, result):
        data = pd.DataFrame(result, columns=self.mycolumns)
        data.to_csv(self.brandName + '.csv', \
                    encoding=self.myencoding, index=True)

    def __init__(self, brandName, url):
        self.brandName = brandName
        self.url = url

        self.mycolumns = ['brand', 'store', 'sido', 'gungu', 'address']

        if self.brandName in ['pelicana']:
            self.mycolumns.append('phone')

        elif self.brandName in ['nene', 'cheogajip', 'goobne']:
            self.mycolumns.append('phone')

        else:
            pass

        if self.brandName != 'goobne':
            self.soup = self.get_request_url()
            self.driver = None
        else:  # 굽네 매장
            self.soup = None
            # filepath = 'c:/chromedriver.exe'
            filepath = '/Users/lune/chromedriver_mac64/chromedriver'
            self.driver = webdriver.Chrome(filepath)
            self.driver.get(self.url)
        # print('생성자 호출됨')
# end class ChickenStore()