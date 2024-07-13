from django.db import models

class Pokemon(models.Model):
    name = models.CharField(max_length=20),
    power = models.CharField(max_lenght=20),
    photo_url =  models.URLField()

    def __str__(self):
        return self.name
