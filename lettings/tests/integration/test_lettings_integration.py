import pytest
from django.urls import reverse
from lettings.models import Address, Letting


@pytest.mark.django_db
def test_index_integration(client):
    """
    Test d'intégration pour la vue index de lettings.
    Vérifie que la page d'index affiche la liste des lettings.
    """
    # Création d'objets de test dans la base de données
    address = Address.objects.create(
        number=10,
        street='Test Street',
        city='Test City',
        state='TS',
        zip_code=12345,
        country_iso_code='TST'
    )
    Letting.objects.create(title='Test Letting', address=address)

    response = client.get(reverse('lettings:index'))
    assert response.status_code == 200
    assert 'Test Letting' in response.content.decode()


@pytest.mark.django_db
def test_letting_integration(client):
    """
    Test d'intégration pour la vue de détail d'un letting.
    Vérifie que la page de détail affiche les informations correctes.
    """
    address = Address.objects.create(
        number=20,
        street='Another Street',
        city='Another City',
        state='AS',
        zip_code=54321,
        country_iso_code='ATS'
    )
    letting = Letting.objects.create(title='Another Letting', address=address)

    response = client.get(reverse('lettings:letting', args=[letting.id]))
    assert response.status_code == 200
    assert 'Another Letting' in response.content.decode()
    assert 'Another Street' in response.content.decode()
