from django.db import models

class Route(models.Model):
    nom= models.CharField(max_length=100)
    longueur= models.FloatField() #long max route
    capacite_max= models.IntegerField() #nbre max vehicule

class Intersection(models.Model):
    nom= models.CharField(max_length=100)
    etat_feu= models.CharField(max_length=20, default='Vert') #pour la phase doptimisation
