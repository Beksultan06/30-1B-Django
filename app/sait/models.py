from django.db import models

# Create your models here.
class Settings(models.Model):
    title = models.CharField(
        max_length=155,
        verbose_name='Заголовок'
    )
    description = models.TextField(
        verbose_name='Описание'
    )
    image = models.ImageField(
        upload_to='settings',
        verbose_name='Фото'
    )
    facebook = models.URLField(
        verbose_name='FaceBook',
        help_text='URL FaceBook'
    )
    twitter = models.URLField(
        verbose_name='Twitter',
        help_text='URL Twitter'
    )
    github = models.URLField(
        verbose_name='GitHub',
        help_text='URL GitHub'
    )
    google = models.URLField(
        verbose_name='Google',
        help_text='URL Google'
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Баннер'
        verbose_name_plural = 'Баннеры'