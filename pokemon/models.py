from django.db import models

class Pokemon(models.Model):
    name = models.CharField(max_length=20, default="wow")
    power = models.CharField(max_length=20, default="magnetism")
    photo_url =  models.URLField(default="www.google.com")

    def __str__(self):
        return self.name
