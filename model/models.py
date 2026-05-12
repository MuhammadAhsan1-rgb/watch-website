from django.db import models

class watchesdata1(models.Model):
    image = models.ImageField(upload_to='products/')
    title = models.CharField(max_length=20)
    company  = models.CharField(max_length=20)
    model = models.CharField(max_length=20)
    machine = models.CharField(max_length=20)
    price = models.IntegerField()
