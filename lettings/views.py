from django.shortcuts import render, get_object_or_404
from .models import Letting


def index(request):
    """
    Vue pour afficher la liste de toutes les propriétés (lettings).

    Récupère toutes les propriétés disponibles et les transmet au template 'lettings/index.html'.
    """
    lettings_list = Letting.objects.all()
    context = {'lettings_list': lettings_list}
    return render(request, 'lettings/index.html', context)


def letting(request, letting_id):
    """
    Vue pour afficher les détails d'une propriété spécifique.

    Récupère une propriété par son ID et
    transmet ses informations au template 'lettings/letting.html'.
    Si la propriété n'est pas trouvée, renvoie une erreur 404.
    """
    letting = get_object_or_404(Letting, id=letting_id)
    context = {
        'title': letting.title,
        'address': letting.address,
    }
    return render(request, 'lettings/letting.html', context)
