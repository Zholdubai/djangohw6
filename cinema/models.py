from django.db import models
from django.utils import timezone


class Director(models.Model):
    name = models.CharField(max_length=100)
    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'

    def __str__(self):
        return self.name

class Movie(models.Model):
    image = models.ImageField(upload_to='movie', null=True)
    title = models.CharField(max_length=255, verbose_name='Названия')
    descriptions = models.TextField( blank=True, verbose_name='Описание')
    created_at = models.DateTimeField( auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')
    director = models.ForeignKey(Director, on_delete=models.PROTECT, verbose_name='Жанр')

    class Meta:
        ordering = ['title', 'descriptions', 'created_at', 'updated_at']
        verbose_name_plural = 'Кино'
        verbose_name = 'Кино'


    def __str__(self):
        return self.title

class Review(models.Model):
    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'

    author = models.CharField(max_length=100)
    text = models.TextField()
    movie = models.ForeignKey(Movie, on_delete=models.PROTECT)

    def __str__(self):
        return self.author