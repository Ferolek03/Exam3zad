from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    image = models.ImageField(upload_to='media/')

    def __str__(self):
        return self.name


class AdvUser(AbstractUser):
    middle_name = models.CharField('Отчество', max_length=50)
    last_name = models.CharField(max_length=12, verbose_name="Фамилия", validators=[
        RegexValidator(regex=r'[а-яА-ЯёЁ]+$', message='Фамилия введена не правильно',
                       code='invalid_last_name'), ])
    first_name = models.CharField(max_length=12, verbose_name="Имя", validators=[
        RegexValidator(regex=r'[а-яА-ЯёЁ]+$', message='Имя введено не правильно',
                       code='invalid_first_name'), ])
    middle_name = models.CharField(max_length=12, verbose_name="Отчество", validators=[
        RegexValidator(regex=r'[а-яА-ЯёЁ]+$', message='Отвество введено не правильно',
                       code='invalid_middle_name'), ])
    role = models.CharField(max_length=254, verbose_name='Роль',
                            choices=(('admin', 'Администратор'), ('user', 'Пользователь'), ('author', 'Автор')),
                            default='user')
    username = models.CharField(max_length=20, verbose_name="Имя пользователя", unique=True, validators=[
        RegexValidator(regex=r'^[a-z]+$', message='Имя пользователя введено не правильно',
                       code='invalid_username'), ])