from django.db import models

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=255)

    class Meta:
        ordering = ('title',)
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.title


class Toner(models.Model):
    title = models.CharField(max_length=255)
    category = models.ForeignKey(Category, related_name='toners', on_delete=models.CASCADE)
    color = models.CharField(max_length=30)
    price = models.IntegerField()
    stock = models.IntegerField()
    description = models.TextField(max_length=255)
    imageUrl = models.URLField()
    status = models.BooleanField(default=True)
    date_created = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ('-date_created',)
    
    def __str__(self):
        return self.title

class Product(models.Model):
    product_tag = models.CharField(max_length=10)
    title = models.CharField(max_length=255)
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    price = models.IntegerField()
    stock = models.IntegerField()
    description = models.TextField(max_length=255)
    imageUrl = models.URLField()
    status = models.BooleanField(default=True)
    date_created = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ('-date_created',)
    
    def __str__self(self):
        return '{} {}'.format(self.product_tag, self.name)