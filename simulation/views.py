from django.shortcuts import render



def simulation_view(request):
    return render(request, 'simulation/index.html')

def stats_view(request):
    return render(request, 'modules_stats.html')

import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import TrafficStats

@csrf_exempt
def api_save_traffic_stats(request):
    if request.method == 'POST':
        try:
            # Récupération des données envoyées par le JS
            data = json.loads(request.body)
            
            # Création de l'entrée en base de données
            TrafficStats.objects.create(
                markov_state=data.get('markovState', 'N/A'),
                capacity_usage=float(data.get('capacityUsage', 0)),
                active_cars=int(data.get('activeCars', 0)),
                system_efficiency=float(data.get('systemEfficiency', 0)),
                spawn_rate=float(data.get('spawnObservedRate', 0))
            )
            
            return JsonResponse({"status": "success", "message": "Données enregistrées"}, status=201)
        except Exception as e:
            return JsonResponse({"status": "error", "message": str(e)}, status=400)
            
    return JsonResponse({"status": "error", "message": "Méthode non autorisée"}, status=405)