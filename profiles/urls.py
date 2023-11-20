from django.urls import path
from . import views

app_name = 'profiles'


urlpatterns = [

    # Cette URL dirige vers la vue 'index' qui affiche la liste des profiles
    path('', views.index, name='index'),

    # 'username' est un paramètre dynamique qui permet d'accéder au détail d'un profile
    path('<str:username>/', views.profile, name='profile'),
]
