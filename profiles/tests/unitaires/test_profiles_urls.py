import pytest
from django.urls import reverse, resolve
from profiles import views


@pytest.mark.django_db
def test_index_url():
    """
    Teste que l'URL de l'index des profils mène à la vue correcte.
    """
    url = reverse('profiles:index')
    assert url == '/profiles/'
    assert resolve(url).func == views.index


@pytest.mark.django_db
def test_profile_url():
    """
    Teste que l'URL de détail d'un profil mène à la vue correcte.
    Utilisation d'un nom d'utilisateur fictif pour le test.
    """
    url = reverse('profiles:profile', args=['testuser'])
    assert url == '/profiles/testuser/'
    assert resolve(url).func == views.profile
