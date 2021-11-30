from textwrap import dedent, indent
import sqlite3
from bs4 import BeautifulSoup
import requests
import uuid
import os
import base64
import enum
from datetime import datetime


class ParserHabr:
    @staticmethod
    def parse(lastDateParse):
        global news

        page = 1
        flag = True

        while flag:
            url = "{}/news_frame/page{}/".format(URL.BASE_HABR.value, page)
            news = []
            try:
                response = requests.get(url, headers=Settings.headers)
                soup = BeautifulSoup(response.content, 'html.parser')
                items = soup.findAll('article', class_='tm-articles-list__item')
                for item in items:
                    date = item.find("time").get("datetime")
                    #if (date < lastDateParse):
                    #    raise ValueError

                    title = item.find("h2", class_="tm-article-snippet__title tm-article-snippet__title_h2").find("span").text
                    description = item.find("div", class_="article-formatted-body article-formatted-body_version-2").find("p").text
                    img = None
                    try:
                        urlImage = "{}".format(item.find("img", class_="tm-article-snippet__lead-image")["src"])
                        print(urlImage)
                        img = Utils.convertImage(urlImage)[:15]
                    except TypeError:
                        img = None

                    post = News(date, title, description, img, REPORTER.HABR_REPORTER.value)
                    news.append(post)

                page += 1
                Utils.saveToDataBase(news)
                falg = False

            #except ValueError:
            #    flag = False
            #    print("Новость с такой датой уже была спарсена")

            except TypeError:
                print("Последняя страница достигнута")
                Utils.saveToDataBase(news)
                flag = False

        print("End parse habr")
        return []

class ParserKuzbassOnline:

    @staticmethod
    def parse(lastDateParse, connect):
        global news
        page = 1
        flag = True
        TOTAL_POSTS = 0
        news = []

        while flag:
            url = "{}/news?feedType=news&page={}#/".format(URL.BASE_KUZBASS_ONLINE.value, page)
            try:
                response = requests.get(url, headers=Settings.headers)
                soup = BeautifulSoup(response.content, 'html.parser')
                items = soup.find("div", class_="section__card-list card-list card-list--col-4").findAll("a")
                if (len(items) == 0):
                    raise Exception

                for item in items:
                    date = item.find("p", class_="feed-card__date").text.split()[0]
                    date = datetime.strptime(date, "%d.%m.%Y")

                    if (date < lastDateParse):
                        raise ValueError

                    urlImage = "{}".format(item.find("img").get("src"))
                    if not ("https" in urlImage):
                        urlImage = "https://online-kuzbass.ru{}".format(urlImage)
                    print(urlImage)
                    img = Utils.convertImage(urlImage)
                    #img = urlImage

                    url_post = "{}{}".format(URL.BASE_KUZBASS_ONLINE.value, item.get("href"))
                    responsePost = requests.get(url_post, headers=Settings.headers)
                    soupPost = BeautifulSoup(responsePost.content, 'html.parser')

                    postElement = soupPost.find("div", class_="post")
                    title = dedent(postElement.find("h1", class_="post__title").text).strip()

                    description = dedent(postElement.find("p", class_="post__text").get_text(separator="<br/>")).strip()
                    short_description = (description[:300] + '...') if len(description) > 75 else description

                    reporter = REPORTER.KUZBASS_ONLINE_REPORTER_ID.value
                    post = News(date.strftime("%Y-%m-%d"), title, description, short_description, img, reporter)
                    news.append(post)
                    print("title: " + title)
                    TOTAL_POSTS += 1

            except ValueError:
                print("Пост уже был спарсен")
                flag = False
                print("TOTAL POSTS: " + str(TOTAL_POSTS))

            except BaseException:
                print("Последняя страница достигнута")
                flag = False
                print("TOTAL POSTS: " + str(TOTAL_POSTS))

            page += 1
            DataBase.saveToDataBase(news, connect)

class News:
    date = ""
    title = ""
    description = ""
    short_description = ""
    img = ""
    reporter = ""

    def __init__(self, date, title, description, short_description, img, reporter):
        self.date = date
        self.title = title
        self.description = description
        self.short_description = short_description
        self.img = img
        self.reporter = reporter

class Utils:

    @staticmethod
    def convertImage(url):
        pathImage = Utils.downloadImg(url)
        # blob = Utils.convertToBlob(pathImage)
        # Utils.deleteFile(pathImage)
        # return blob
        return pathImage

    # @staticmethod
    # def convertToBlob(pathImg):
    #     img = open(pathImg, 'rb')
    #     blob = img.read()
    #     return blob

    @staticmethod
    def downloadImg(url):

        fileName = Settings.basePackageImg + str(uuid.uuid4()) + ".jpg"
        r = requests.get(url, allow_redirects=True)
        # Сохранение изображения файлом
        open(fileName, 'wb').write(r.content)

        return fileName

    @staticmethod
    def deleteFile(path):
        os.remove(path)

class DataBase:
    @staticmethod
    def create_connection(path):
        connection = None
        try:
            connection = sqlite3.connect(path)
            print("Connection to SQLite DB successful")
        except Exception as e:
            print(f"The error '{e}' occurred")

        return connection

    @staticmethod
    def saveToDataBase(posts, connect):
        for item in posts:
            cursor = connect.cursor()
            cursor.execute("INSERT INTO main_posts (date, title, description, short_description, image, reporter_id, viewers) VALUES(?, ?, ?, ?, ?, ?, ?)", [item.date, item.title, item.description, item.short_description, item.img, item.reporter, 0])
            connect.commit()
            cursor.close()

        print("save")

    @staticmethod
    def saveLastDateParseTodataBase(date, connect):
        cursor = connect.cursor()
        query = "INSERT INTO main_datelastparse (lastDate) VALUES ('{}')".format(datetime.strftime(date, "%d-%m-%Y"))
        cursor.execute(query)
        connect.commit()
        cursor.close()

    @staticmethod
    def getLastDateParse(connect, startDate):
        global date
        try:
            cursor = connect.cursor()
            query = "SELECT lastDate FROM main_datelastparse ORDER BY id DESC LIMIT 1"
            date = cursor.execute(query).fetchall()[0][0]
            cursor.close()
        except Exception as e:
            date = "01-01-2018"#startDate.strftime("%d-%m-%Y")
            print("Last date is not found in database")

        return datetime.strptime(date, "%d-%m-%Y") # datetime.strptime("01-01-2018", "%d-%m-%Y")

class URL(enum.Enum):
    BASE_HABR = "https://habr.com/ru"
    BASE_KUZBASS_ONLINE = "https://kemerovo.kuzbass-online.ru"

class REPORTER(enum.Enum):
    HABR_REPORTER = "HABR"
    KUZBASS_ONLINE_REPORTER = "KUZBASS_ONLINE"

    KUZBASS_ONLINE_REPORTER_ID = 1


class Settings:

    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 11.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/92.0.4515.159 Safari/537.36 Edg/92.0.902.84 '
    }

    pathToDatabaseFile = "../TopNews/db.sqlite3"

    basePackageImg = "../TopNews/media/"

connect = DataBase.create_connection(Settings.pathToDatabaseFile)


startDateParse = datetime.strptime(datetime.now().date().__str__(), "%Y-%m-%d")
lastDateParse = DataBase.getLastDateParse(connect, startDateParse)

# Сюда вписывать все парсеры
ParserKuzbassOnline.parse(lastDateParse, connect)


#сделать запись о последнем парсинге
DataBase.saveLastDateParseTodataBase(startDateParse, connect)