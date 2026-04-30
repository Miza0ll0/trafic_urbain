from django.db import models

class Route(models.Model):
    nom= models.CharField(max_length=100)
    longueur= models.FloatField() #long max route
    capacite_max= models.IntegerField() #nbre max vehicule

class Intersection(models.Model):
    nom= models.CharField(max_length=100)
    etat_feu= models.CharField(max_length=20, default='Vert') #pour la phase doptimisation


from django.db import models

from django.db import models

class TrafficStats(models.Model):
    # Date et heure de l'enregistrement
    date_save = models.DateTimeField(auto_now_add=True)
    
    # Données techniques
    markov_state = models.CharField(max_length=50, verbose_name="État Markov")
    capacity_usage = models.FloatField(verbose_name="Occupation %")
    active_cars = models.IntegerField(verbose_name="Véhicules Actifs")
    system_efficiency = models.FloatField(verbose_name="Efficacité %")
    spawn_rate = models.FloatField(verbose_name="Taux de Spawn")

    class Meta:
        ordering = ['-date_save'] # Les plus récents en premier

    def __str__(self):
        return f"Stats du {self.date_save.strftime('%d/%m/%Y %H:%M')}"