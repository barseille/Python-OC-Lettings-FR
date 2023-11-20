from django.shortcuts import render
import logging

# Configuration du logger
logger = logging.getLogger(__name__)


def home(request):
    """
    Vue pour la page d'accueil du site.

    Affiche la page d'accueil principale du site web.
    """
    try:
        return render(request, 'base.html')
    except Exception as e:
        logger.error(f"Erreur dans la vue home: {e}", exc_info=True)


def custom_404(request, _exception):
    """
    Vue personnalisée pour l'erreur 404 (page non trouvée).

    Affiche une page d'erreur 404 personnalisée
    lorsque l'utilisateur demande une page qui n'existe pas.

    paramètre '_exception' est requis par la signature de la fonction
    mais n'est pas utilisé dans le corps de la fonction
    """
    try:
        return render(request, '404.html', status=404)
    except Exception as e:
        logger.error(f"Erreur dans la vue custom_404: {e}", exc_info=True)


def custom_500(request):
    """
    Vue personnalisée pour l'erreur 500 (erreur serveur interne).

    Affiche une page d'erreur 500 personnalisée en cas de problème interne du serveur.
    """
    try:
        return render(request, '500.html', status=500)
    except Exception as e:
        logger.error(f"Erreur dans la vue custom_500: {e}", exc_info=True)
