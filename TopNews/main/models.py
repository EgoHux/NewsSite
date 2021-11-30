from django.db import models


# python manage.py makemigrations
# python manage.py migrate


# Create your models here.
from setuptools.command.upload import upload


class Roles(models.Model):
    nameRole = models.CharField(max_length=20)


# models.CASCADE: автоматически удаляет строку из зависимой таблицы, если удаляется связанная строка из главной таблицы

# models.PROTECT: блокирует удаление строки из главной таблицы, если с ней связаны какие-либо строки из зависимой таблицы

# models.SET_NULL: устанавливает NULL при удалении связанной строка из главной таблицы

# models.SET_DEFAULT: устанавливает значение по умолчанию для внешнео ключа в зависимой таблице. В этом случае для этого столбца должно быть задано значение по умолчанию

# models.DO_NOTHING: при удалении связанной строки из главной таблицы не производится никаких действий в зависимой таблице


class Users(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    login = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    role = models.ForeignKey(Roles, null=True, on_delete=models.SET_NULL)
    image = models.ImageField(upload_to='media/', null=True)

class Sites(models.Model):
    name = models.CharField(max_length=30)
    base_url = models.TextField()

class Reporters(models.Model):
    user = models.ForeignKey(Users, null=True, on_delete=models.SET_NULL, db_constraint=False)
    site = models.ForeignKey(Sites, null=True, on_delete=models.SET_NULL, db_constraint=False)

class Posts(models.Model):
    reporter = models.ForeignKey(Reporters, null=True, on_delete=models.SET_NULL)
    date = models.DateField()
    title = models.CharField(max_length=30)
    short_description = models.TextField()
    description = models.TextField()
    image = models.ImageField(upload_to="media/")
    viewers = models.IntegerField()


class Likes(models.Model):
    user = models.ForeignKey(Users, null=True, on_delete=models.SET_NULL)
    post = models.ForeignKey(Posts, null=True, on_delete=models.SET_NULL)
    rate = models.BooleanField(null=True)


class Comments(models.Model):
    user = models.ForeignKey(Users, null=True, on_delete=models.SET_NULL)
    post = models.ForeignKey(Posts, null=True, on_delete=models.SET_NULL)
    date = models.DateField()
    text = models.TextField()

class DateLastParse(models.Model):
    lastDate = models.TextField()





