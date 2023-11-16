from django.shortcuts import render


def home(request):
    """
    Vue pour la page d'accueil du site.

    Affiche la page d'accueil principale du site web.
    """
    return render(request, 'base.html')


def custom_404(request, _exception):
    """
    Vue personnalisée pour l'erreur 404 (page non trouvée).

    Affiche une page d'erreur 404 personnalisée
    lorsque l'utilisateur demande une page qui n'existe pas.

    paramètre '_exception' est requis par la signature de la fonction
    mais n'est pas utilisé dans le corps de la fonction
    """
    return render(request, '404.html', status=404)


def custom_500(request):
    """
    Vue personnalisée pour l'erreur 500 (erreur serveur interne).

    Affiche une page d'erreur 500 personnalisée en cas de problème interne du serveur.
    """
    return render(request, '500.html', status=500)
