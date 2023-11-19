from django.http import HttpRequest
from oc_lettings_site.views import home, custom_404, custom_500


def test_home_view():
    """
    Teste la vue 'home' pour s'assurer qu'elle renvoie une réponse HTTP 200
    et qu'elle utilise le bon template (base.html).
    """
    # Arrange
    request = HttpRequest()

    # Act
    response = home(request)

    # Assert
    assert response.status_code == 200

    # 'b' devant la chaîne de caractères indique qu'il s'agit d'une chaîne de caractères en bytes
    assert b"Welcome to Holiday Homes" in response.content


def test_custom_404_view():
    """
    Teste la vue personnalisée pour l'erreur 404 pour s'assurer qu'elle renvoie
    une réponse HTTP 404 et qu'elle affiche le contenu approprié.
    """
    # Arrange
    request = HttpRequest()
    exception = Exception()

    # Act
    response = custom_404(request, exception)

    # Assert
    assert response.status_code == 404
    assert b"Nous ne pouvons pas trouver la page que vous cherchez." in response.content


def test_custom_500_view():
    """
    Teste la vue personnalisée pour l'erreur 500 pour s'assurer qu'elle renvoie
    une réponse HTTP 500 et qu'elle affiche le contenu approprié.
    """
    # Arrange
    request = HttpRequest()

    # Act
    response = custom_500(request)

    # Assert
    assert response.status_code == 500
    assert b"Oups! Erreur interne du serveur." in response.content
