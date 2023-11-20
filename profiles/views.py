from django.shortcuts import render, get_object_or_404, Http404
from .models import Profile
import logging

logger = logging.getLogger(__name__)


def index(request):
    """
    Vue pour afficher la liste de tous les profils utilisateurs.

    Récupère tous les profils disponibles et les transmet au template 'profiles/index.html'.
    """
    try:
        profiles_list = Profile.objects.all()
    except Exception:
        logger.error("Erreur lors de la récupération des profils", exc_info=True)
    else:
        context = {'profiles_list': profiles_list}
        return render(request, 'profiles/index.html', context)


def profile(request, username):
    """
    Vue pour afficher les détails d'un profil utilisateur spécifique.

    Récupère un profil par son nom d'utilisateur et
    transmet ses informations au template 'profiles/profile.html'.
    Si le profil n'est pas trouvé, renvoie une erreur 404.
    """
    try:
        profile = get_object_or_404(Profile, user__username=username)
    except Http404 as e:
        logger.error(f"Erreur lors de la récupération du profil {username}", exc_info=True)
        raise e
    else:
        context = {'profile': profile}
        return render(request, 'profiles/profile.html', context)
