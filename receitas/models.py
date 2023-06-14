from django.db import models

# Create your models here.
class Receita (models.Model):
    receita  = models.CharField(max_length = 100)
    def __str__(self):
        return self.receita
    

class Log(models.Model):
    IP = models.CharField(max_length=200)
    acesso = models.CharField(max_length=200)
    latitude = models.CharField(max_length=200)
    longitude = models.CharField(max_length=200)
    sistema = models.CharField(max_length=200)
    def __str__(self):
        return self.IP ,self.acesso,self.latitude,self.longitude,self.sistema 

class Livro(models.Model):
    titulo = models.CharField(max_length=400)
    isbn = models.CharField(max_length=400)
    editora = models.CharField(max_length=400)
    autor = models.CharField(max_length=400)
    versao_fisica = models.BooleanField(True)

    def __str__(self):
        return self.titulo ,self.isbn,self.editora,self.autor,self.versao_fisica