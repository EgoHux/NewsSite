from bs4 import BeautifulSoup
import requests
import uuid
import os
import base64
import enum    

class ParserHabr:
    
    def start():
        print("Здесь будет точка входа")

    def parse():
        response = requests.get(Settings.url["BASE_HABR"], headers=Settings.headers)
        soup = BeautifulSoup(response.content, 'html.parser')
        items = soup.findAll('article', class_='tm-articles-list__item')
        news = []



        print("parse habr")

class ParserName:
    def parse():
        print("parse name")
    

class News:
    date = ""
    title = ""
    description = ""
    img = ""
    reporter = ""

    def __init__(self, date, title, description, img, reporter):
        self.date = date
        self.title = title
        self.description = description
        self.img = img
        self.reporter = reporter

class Utils:
    def convertToBlob(pathImg):
        img = open(pathImg, 'rb').read()
        blob = base64.encodebytes(img)

        print("перевожу скачанную img в blob")
        return blob

    def downloadImg(url):

        fileName = Settings.basePackageImg + str(uuid.uuid4()) + ".jpg"
        r = requests.get(url, allow_redirects=True)
        # Сохранение изображения файлом
        open(fileName, 'wb').write(r.content)

        return fileName

    def deleteFile(path):
        os.remove(path)
        print("удалить img после записи в БД")

    def saveToDataBase(newsList):
        # логика сохранения в БД через ОРМ
        print("save")

    def getParseLastDate():
        print("LastDate")
        # возвращение последней даты парсинга. Будем в БД хранить ее
        

class Settings:
    url = {
        "BASE_HABR": "https://habr.com/ru/news/",
        "123": "123",
        "site": "site"
    }

    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/92.0.4515.159 Safari/537.36 Edg/92.0.902.84 '
    }

    basePackageImg = "D://"

    # креды от dataBase сюда же можно написать


#news = News("1", "2", "3", "4")
ParserHabr.parse()
#path = Utils.downloadImg("https://img5.goodfon.ru/wallpaper/nbig/3/73/abstraktsiia-antisfera-vodovorot-krasok-kartinka-chernyi-fon.jpg")
#f = Utils.convertToBlob(path)
#Utils.deleteFile(path)
#print(f)

        
        

        