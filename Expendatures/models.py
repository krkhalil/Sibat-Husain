from django.db import models
class expendature(models.Model):
    Reciept_No = models.CharField(max_length=10)
    Amount = models.IntegerField()
    Purpose = models.TextField(blank=True)
    def __str__(self):
        return self.Reciept_No
