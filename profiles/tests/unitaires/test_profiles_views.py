import pytest
from django.urls import reverse


@pytest.mark.django_db
def test_index_view(client):
    """
    Teste la vue index de l'application profiles.
    Vérifie que la réponse HTTP est 200, que le bon template est utilisé,
    et que le contexte contient une liste de profils.
    """
    url = reverse('profiles:index')
    response = client.get(url)
    assert response.status_code == 200
    assert 'profiles/index.html' in [element.name for element in response.templates]
    assert 'profiles_list' in response.context


@pytest.mark.django_db
def test_profile_view(client, profile):
    """
    Teste la vue profile de l'application profiles.

    Vérifie que la réponse HTTP est 200 pour un nom d'utilisateur valide,
    que le bon template est utilisé, et que le contexte contient
    les détails du profil spécifié.

    Teste également que la vue renvoie une réponse 404 pour un nom d'utilisateur invalide.
    """
    url = reverse('profiles:profile', args=[profile.user.username])
    response = client.get(url)
    assert response.status_code == 200
    assert 'profiles/profile.html' in [element.name for element in response.templates]
    assert response.context['profile'] == profile

    # Test pour un nom d'utilisateur invalide
    invalid_url = reverse('profiles:profile', args=['nonexistentuser'])
    response = client.get(invalid_url)
    assert response.status_code == 404
