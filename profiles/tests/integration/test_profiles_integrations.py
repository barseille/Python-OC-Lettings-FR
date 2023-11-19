import pytest
from django.urls import reverse
from django.contrib.auth.models import User
from profiles.models import Profile


@pytest.mark.django_db
def test_index_integration(client):
    """
    Test d'intégration pour la vue index de profiles.
    Vérifie que la page d'index affiche la liste des profils.
    """
    # Création d'un utilisateur de test dans la base de données
    user = User.objects.create_user(username='testuser', password='12345')
    Profile.objects.create(user=user, favorite_city="Test City")

    response = client.get(reverse('profiles:index'))
    assert response.status_code == 200
    assert 'testuser' in response.content.decode()


@pytest.mark.django_db
def test_profile_integration(client):
    """
    Test d'intégration pour la vue de détail d'un profil.
    Vérifie que la page de détail affiche les informations correctes.
    """
    user = User.objects.create_user(username='anotheruser', password='12345')
    profile = Profile.objects.create(user=user, favorite_city="Another City")

    response = client.get(reverse('profiles:profile', args=[profile.user.username]))
    assert response.status_code == 200
    assert 'anotheruser' in response.content.decode()
    assert 'Another City' in response.content.decode()
