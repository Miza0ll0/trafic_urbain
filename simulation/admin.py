from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import TrafficStats

@admin.register(TrafficStats)
class TrafficStatsAdmin(admin.ModelAdmin):
    # Les colonnes qui seront affichées dans la liste
    list_display = ('date_save', 'markov_state', 'active_cars', 'capacity_usage')
    # Ajouter un filtre par date sur le côté
    list_filter = ('date_save', 'markov_state')