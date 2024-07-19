from django.contrib.auth.models import User
from django.db import models


class Food(models.Model):
    name = models.CharField(max_length=60)
    info = models.TextField(blank=True)
    manufacture = models.TextField(blank=True)
    cat = models.ForeignKey('Category', models.PROTECT)
    user = models.ForeignKey(User, verbose_name="Users", on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=60)

    def __str__(self):
        return self.name




