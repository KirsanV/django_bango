from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=200, verbose_name='Заголовок')
    content = models.TextField(verbose_name='Содержание статьи')
    preview_image = models.ImageField(upload_to='blog_previews/', verbose_name='Превью изображения')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    is_published = models.BooleanField(default=False, verbose_name='Опубликовать')
    views_count = models.PositiveIntegerField(default=0, verbose_name='Количество просмотров')

    class Meta:
        verbose_name = 'Блоговая запись'
        verbose_name_plural = 'Блоговые записи'

    def __str__(self):
        return self.title