from django.test import Client
import pytest


def test_home_page():
    """
    Teste si la page d'accueil est accessible et renvoie un code de statut HTTP 200.
    """
    client = Client()
    response = client.get('/')
    assert response.status_code == 200


@pytest.mark.django_db
def test_lettings_page():
    """
    Teste si la page des lettings est accessible et renvoie un code de statut HTTP 200.
    """
    client = Client()
    response = client.get('/lettings/')
    assert response.status_code == 200


@pytest.mark.django_db
def test_profiles_page():
    """
    Teste si la page des profils est accessible et renvoie un code de statut HTTP 200.
    """
    client = Client()
    response = client.get('/profiles/')
    assert response.status_code == 200


@pytest.mark.django_db
def test_admin_redirect():
    """
    Teste si l'accès à la page admin redirige (code de statut HTTP 302).
    """
    client = Client()
    response = client.get('/admin/')
    assert response.status_code == 302
