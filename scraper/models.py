from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=200)
    reference = models.CharField(max_length=100)
    sku = models.CharField(max_length=50)

class SearchResults(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    url_google_shopping = models.URLField()
    id_casa_del_electrodomestico = models.CharField(max_length=50)
    joined_date = models.DateField(null=False)
