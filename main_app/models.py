from django.db import models


class Widget(models.Model):
    description = models.CharField(max_length=255)
    quantity = models.IntegerField(default=1)
# Create your models here.
  