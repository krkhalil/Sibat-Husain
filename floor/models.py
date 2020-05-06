from django.db import models


class floor(models.Model):
    name = models.CharField(max_length=200)
    NO_OF_Rooms = models.IntegerField()
    def __str__(self):
        return self.name
