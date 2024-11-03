from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    email = models.EmailField(
        unique=True,
        verbose_name='Email'
        )

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.username


class Task(models.Model):
    user = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        verbose_name='Пользователь'
        )
    title = models.CharField(
        max_length=50,
        verbose_name='Название задачи'
        )
    description = models.TextField(
        blank=True,
        verbose_name='Описание'
        )
    complete_status = models.BooleanField(
        default=False,
        verbose_name='Статус выполнения'
        )
    create = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата создания'
        )

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'
        ordering = ['complete_status', '-create']

    def __str__(self):
        return self.title
