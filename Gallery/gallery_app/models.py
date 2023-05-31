from django.db import models

# Create your models here.

class Photo(models.Model):
    file_name = models.CharField('Название файла фото', max_length = 250)
    like_counter = models.IntegerField('Кол-во лайков')
    def __str__(self):
        return self.file_name
    
class Comment(models.Model):
    author = models.CharField('Автор комментария', max_length = 250)
    comment_text = models.CharField('Текст комментария', max_length = 250)
    photo_id = models.ForeignKey(Photo, on_delete=models.CASCADE, null = True, blank = True)
    def __str__(self):
        return self.comment_text