from django.db import models


class Author(models.Model):
    name = models.CharField(
        max_length=155,
        verbose_name='Имя'
    )
    email = models.EmailField(
        verbose_name='Почта'
    )
    birth_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'    