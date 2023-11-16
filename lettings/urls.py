from django.urls import path
from . import views

# Espace de noms pour les URL d'une application spécifique
app_name = 'lettings'

urlpatterns = [

    # Cette URL dirige vers la vue 'index' qui affiche la liste des lettings
    path('', views.index, name='index'),

    # 'letting_id' est un paramètre dynamique qui permet d'accéder au détail d'un letting.
    path('<int:letting_id>/', views.letting, name='letting'),
]
