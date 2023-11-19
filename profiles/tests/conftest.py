import pytest
from django.contrib.auth.models import User
from profiles.models import Profile
from django.test import Client


@pytest.fixture
def user():
    """
    Crée et renvoie une instance du modèle User pour les tests.
    """
    return User.objects.create_user(username='testuser', password='12345')


@pytest.fixture
def profile(user):
    """
    Crée et renvoie une instance du modèle Profile pour les tests, en utilisant la fixture 'user'.
    """
    return Profile.objects.create(user=user, favorite_city="Paris")


@pytest.fixture
def client():
    """
    Instance de Client Django pour simuler les requêtes HTTP dans les tests.
    """
    return Client()
