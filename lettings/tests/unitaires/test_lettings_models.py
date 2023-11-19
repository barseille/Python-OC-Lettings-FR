import pytest
from django.test import Client
from lettings.models import Address, Letting


@pytest.fixture
@pytest.mark.django_db
def address():
    """
    Instance de modèle Address pour les tests.
    """
    return Address.objects.create(
        number=10,
        street='Avenue des champs élysées',
        city='Paris',
        state='île de France',
        zip_code=75008,
        country_iso_code='FRANCE'
    )


@pytest.fixture
@pytest.mark.django_db
def letting(address):
    """
    Instance de modèle Letting pour les tests, en utilisant la fixture 'address'.
    """
    return Letting.objects.create(
        title='Place de Paris',
        address=address
    )


@pytest.fixture
def client():
    """
    Instance de Client Django pour simuler les requêtes HTTP dans les tests.
    """
    return Client()
