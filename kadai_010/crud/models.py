from django.db import models
from django.urls import reverse

# Create your models here.
class Product(models.Model):
    name=models.CharField(max_length=200)
    price=models.PositiveBigIntegerField()

    def __str__(self):
        return self.name
    
    # 新規作成、編集完了時のダイレクト先
    def get_absolute_url(self):
        return reverse('list')