from django.shortcuts import render, get_object_or_404
from .models import Profile


def index(request):
    """
    Vue pour afficher la liste de tous les profils utilisateurs.

    Récupère tous les profils disponibles et les transmet au template 'profiles/index.html'.
    """
    profiles_list = Profile.objects.all()
    context = {'profiles_list': profiles_list}
    return render(request, 'profiles/index.html', context)


def profile(request, username):
    """
    Vue pour afficher les détails d'un profil utilisateur spécifique.

    Récupère un profil par son nom d'utilisateur et
    transmet ses informations au template 'profiles/profile.html'.
    Si le profil n'est pas trouvé, renvoie une erreur 404.
    """
    profile = get_object_or_404(Profile, user__username=username)
    context = {'profile': profile}
    return render(request, 'profiles/profile.html', context)
