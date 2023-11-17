from django.urls import reverse, resolve
from oc_lettings_site import views
from lettings import views as lettings_views
from profiles import views as profiles_views


def test_home_url():
    """
    Teste si l'URL de la page d'accueil est correctement résolue.
    """
    url = reverse('home')
    assert resolve(url).func == views.home


def test_admin_url():
    """
    Teste si l'URL de l'interface d'administration est correctement résolue.
    """
    url = reverse('admin:index')
    assert url.startswith('/admin/')


def test_lettings_index_url():
    """
    Teste si l'URL de l'index de l'application 'lettings' est correctement résolue.
    """
    url = reverse('lettings:index')
    assert resolve(url).func == lettings_views.index


def test_profiles_index_url():
    """
    Teste si l'URL de l'index de l'application 'profiles' est correctement résolue.
    """
    url = reverse('profiles:index')
    assert resolve(url).func == profiles_views.index
