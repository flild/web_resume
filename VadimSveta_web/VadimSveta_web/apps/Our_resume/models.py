from django.db import models

class Our_resume(models.Model):
    pass

class Comment(models.Model):
    comment_autor_name = models.CharField('имя автора', max_length=100)
    comment_text = models.CharField('текст комментария', max_length=300)
    comment_date = models.DateTimeField('дата публикации')
    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'