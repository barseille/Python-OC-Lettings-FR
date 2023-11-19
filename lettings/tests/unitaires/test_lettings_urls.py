import pytest
from django.urls import reverse, resolve
from lettings import views


@pytest.mark.django_db
def test_index_url():
    """
    Teste que l'URL de l'index des lettings mène à la vue correcte.
    """
    url = reverse('lettings:index')
    assert url == '/lettings/'
    assert resolve(url).func == views.index


@pytest.mark.django_db
def test_letting_url():
    """
    Teste que l'URL de détail d'un letting mène à la vue correcte.
    """

    # Utilisation d'un ID fictif pour le test
    url = reverse('lettings:letting', args=[1])
    assert url == '/lettings/1/'
    assert resolve(url).func == views.letting
