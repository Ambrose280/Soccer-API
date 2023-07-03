from django.db import models

class Player(models.Model):
    name = models.CharField(max_length=200)
    country = models.CharField(max_length=20)
    price = models.CharField(max_length=10)

    def __str__(self):
        return self.name
