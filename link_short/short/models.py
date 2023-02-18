from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Link(models.Model):
    author = models.ForeignKey(User, verbose_name='Автор', on_delete=models.CASCADE, default='1')
    title = models.CharField('Название', max_length=30, unique=True)
    start_link = models.URLField('Первоначальная ссылка', max_length=200)
    late_link = models.CharField('Сокращенная ссылка', max_length=30, default='https://clck.ru/9zuXm')

    def get_absolute_url(self):
        return reverse('profile')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Ссылка'
        verbose_name_plural = 'Ссылки'
