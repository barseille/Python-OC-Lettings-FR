from django.shortcuts import render, get_object_or_404, Http404
from .models import Letting
import logging

logger = logging.getLogger(__name__)


def index(request):
    """
    Vue pour afficher la liste de toutes les propriétés (lettings).
    """
    try:
        lettings_list = Letting.objects.all()

    except Exception:
        logger.error("Erreur lors de la récupération des lettings", exc_info=True)

    else:
        context = {'lettings_list': lettings_list}
        return render(request, 'lettings/index.html', context)


def letting(request, letting_id):
    """
    Vue pour afficher les détails d'une propriété spécifique.

    Récupère une propriété par son ID et
    transmet ses informations au template 'lettings/letting.html'.
    Si la propriété n'est pas trouvée, renvoie une erreur 404.
    """
    try:
        letting = get_object_or_404(Letting, id=letting_id)
    except Http404 as e:
        logger.error(f"Erreur lors de la récupération de l'ID {letting_id}", exc_info=True)
        raise e
    else:
        context = {
            'title': letting.title,
            'address': letting.address,
        }
        return render(request, 'lettings/letting.html', context)
