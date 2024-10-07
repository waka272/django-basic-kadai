from django.db import models
from django.urls import reverse

# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Product(models.Model):
    name=models.CharField(max_length=200)
    price=models.PositiveBigIntegerField()
    category=models.ForeignKey(Category, on_delete=models.CASCADE)
    img=models.ImageField(blank=True, default='noImage.png')
    description=models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
    
    # 新規作成、編集完了時のダイレクト先
    def get_absolute_url(self):
        return reverse('list')