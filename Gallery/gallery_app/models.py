from django.db import models

# Create your models here.

class Photo(models.Model):
    file_name = models.CharField('Название файла фото', max_length = 250)
    like_counter = models.IntegerField('Кол-во лайков')