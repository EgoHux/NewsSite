from bs4 import BeautifulSoup
import requests
import pandas as pd

url = "https://habr.com/ru/news/"

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/92.0.4515.159 Safari/537.36 Edg/92.0.902.84 '
}


def count_url(link, count):
    if count == 1:
        print(link)
        return link
    else:
        print(f"{link}page{count}/")
        # return link + "page" + str(count) + "/"
        return f"{link}page{count}/"


def save(var):
    with open('parse_info.txt', 'a') as file:
        # file.write(f'{comp["title"]} \n -> Price: {comp["price"]} \n -> Link: {comp["link"]}')
        file.write(var)


def parse(link):
    response = requests.get(link, headers=headers)

    # response Выводит статус код, а для получения контента нужно использовать метод content
    soup = BeautifulSoup(response.content, 'html.parser')
    # item = Храним элементы сайта с нужным и не нужным содержимым
    items = soup.findAll('article', class_='tm-articles-list__item')

    # new = Список элементов которые мы спарсили
    news = []

    for item in items:
        # Исключение сделал для тупово супа который в конце выдает ошибку None
        try:
            # tst = item.find('div', class_="tm-article-body tm-article-snippet__lead").find('img')
            # print(tst['src'])

            news.append({
                # Берем время выпуска новости
                # 'time': item.find()
                # Берем название новости
                'title': item.find('a', class_='tm-article-snippet__title-link').find('span').get_text(),
                # Берем картинку новости
                'img': item.find('div', class_="tm-article-body tm-article-snippet__lead").find('img').get('src'),
                # 'img': tst['src'],
                # Берем цену клЯпа
                # 'link': item.find('a', class_='btn btn-default add2cart').get('href')
            })
        except AttributeError:
            print("Ошибка")



    for new in news:
        # print(new)

        print(new['title'], new['img'])
        # print(f'{new["title"]} \n -> img: {new["img"]}')
        # save(f'{new["title"]} \n -> Price: {new["price"]} \n -> Link: {new["link"]}\n')


for i in range(1):
    parse(count_url(url, i+1))
