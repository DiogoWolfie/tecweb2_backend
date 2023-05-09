from django.db import models

# Create your models here.
class Receita (models.Model):
    receita  = models.CharField(max_length = 100)
    def __str__(self):
        return self.receita