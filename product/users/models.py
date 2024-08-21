from django.contrib.auth.models import AbstractUser
from django.db import models
from courses.models import Course

class CustomUser(AbstractUser):
    """Кастомная модель пользователя - студента."""

    email = models.EmailField(
        verbose_name='Адрес электронной почты',
        max_length=250,
        unique=True
    )
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = (
        'username',
        'first_name',
        'last_name',
        'password'
    )

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ('-id',)

    def __str__(self):
        return self.get_full_name()


class Balance(models.Model):
    """Модель баланса пользователя."""

    # TODO
    user = models.OneToOneField(to=CustomUser, on_delete=models.CASCADE, primary_key=True, parent_link=True)
    quantity = models.PositiveIntegerField(default=1000)

    class Meta:
        verbose_name = 'Баланс'
        verbose_name_plural = 'Балансы'


class Subscription(models.Model):
    """Модель подписки пользователя на курс."""

    # TODO
    user = models.ForeignKey(to=CustomUser, on_delete=models.CASCADE)
    course = models.ForeignKey(to=Course, on_delete=models.PROTECT)

    class Meta:
        verbose_name = 'Подписка'
        verbose_name_plural = 'Подписки'
        ordering = ('-id',)

