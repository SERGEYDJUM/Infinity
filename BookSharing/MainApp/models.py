from django.db import models

class Books(models.Model):
    image = models.FileField(null=True, blank=True)
    book = models.CharField(max_length=20)
    dis = models.CharField(max_length=120)
    cont = models.CharField(max_length=30)
