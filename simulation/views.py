from django.shortcuts import render



def simulation_view(request):
    return render(request, 'simulation/index.html')
