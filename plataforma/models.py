from datetime import datetime
from django.db import models
from django.forms import DateField

# Create your models here.
class Acidente(models.Model):
    data = models.DateField()
    local = models.TextField()
    nome_funcionario = models.TextField()
    def __str__(self):
        return self.nome_funcionario