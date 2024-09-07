from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=32)

    def __str__(self):
        return self.title


class File(models.Model):
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    title = models.CharField(max_length=128)
    image = models.ImageField()
    file = models.FileField()
    views = models.IntegerField(default=0)
    date = models.DateTimeField(auto_now=True)
    price = models.IntegerField(default=0)

    def __str__(self):
        return self.title


class History(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    file = models.ForeignKey(File, on_delete=models.PROTECT)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.user.username} {self.file.title}'
