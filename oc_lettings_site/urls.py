from django.contrib import admin
from django.urls import path, include
from . import views


# def trigger_error(request):
#     division_by_zero = 1 / 0


urlpatterns = [

    # Chemin d'accès à l'interface d'administration de Django
    path('admin/', admin.site.urls),

    # Chemin d'accès à la page d'accueil du site
    path('', views.home, name='home'),

    # Inclut les chemins d'URL de l'application 'lettings'.
    # Toutes les URL commençant par 'lettings/' seront redirigées vers lettings.urls.
    path('lettings/', include('lettings.urls', namespace='lettings')),

    # Inclut les chemins d'URL de l'application 'profiles'.
    # Toutes les URL commençant par 'profiles/' seront redirigées vers profiles.urls.
    path('profiles/', include('profiles.urls', namespace='profiles')),

    # Test sentry
    # path('sentry-debug/', trigger_error),
]
