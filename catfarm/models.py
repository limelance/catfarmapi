from django.db import models


class Cat(models.Model):
    """
    Модель кота
    """
    name = models.CharField(max_length=30)
    breed = models.CharField(max_length=30)
    age = models.IntegerField()

    HAIRINESS_CHOICES = (('b','bald'), ('s', 'short'), ('l', 'long'))
    hairiness = models.CharField(max_length=1, choices=HAIRINESS_CHOICES)

    owner = models.ForeignKey('auth.User', related_name='cats',on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Кот'
        verbose_name_plural = 'Коты'
