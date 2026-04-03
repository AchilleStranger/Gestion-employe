from django.db import models

class Employe(models.Model):
    nom=models.CharField(max_length=100)
    email=models.EmailField()
    poste=models.CharField(max_length=100)
    salaire=models.DecimalField(max_digits=10, decimal_places=2)
    date_de_naissance=models.DateField(null=True,blank=True)
    lieu_de_residence=models.CharField(max_length=100)
    def __str__(self):
        return self.nom

