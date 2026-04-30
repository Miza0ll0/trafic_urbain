"""
URL configuration for urban_traffic project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


from django.contrib import admin
from django.urls import path
from simulation.views import simulation_view
from simulation.views import stats_view, api_save_traffic_stats

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', simulation_view, name='simulation'),
    path('modules_stats.html', stats_view, name='stats'),
    path('api/save-stats/', api_save_traffic_stats, name='api_save_stats'),
]