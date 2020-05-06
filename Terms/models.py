from django.db import models

class term(models.Model):
    Type_OF = models.CharField(max_length=200)
    Terms = models.TextField(blank=True)
    
    def __str__(self):
        return self.Terms
