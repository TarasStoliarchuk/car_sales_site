from django.db import models
from django.contrib.auth.models import User


class AdvUser(User):
    class Meta(User.Meta):
        pass


class Brands(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, default=0)

    def __str__(self):
        return self.name


class Post(models.Model):
    salesperson = models.ForeignKey(AdvUser, related_name='posts', on_delete=models.CASCADE)
    name = models.CharField(max_length=150, verbose_name='Марка')
    number = models.CharField(max_length=13, verbose_name='Ваш номер')
    image = models.ImageField(upload_to='articles/', verbose_name='Фото')
    mileage = models.IntegerField(default=0, verbose_name='Пробег')
    price = models.IntegerField(default=0, verbose_name='Цена')
    age = models.IntegerField(default=0, verbose_name='Год')
    text = models.TextField(verbose_name='Причина продажи')
    create_at = models.DateTimeField(auto_now_add=True, verbose_name='')
    brand = models.ForeignKey(Brands,
                              on_delete=models.CASCADE,
                              related_name='post',
                              null=False,
                              verbose_name='Бренд'
                              )

