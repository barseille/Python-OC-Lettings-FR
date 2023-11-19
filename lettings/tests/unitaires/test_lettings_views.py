import pytest
from django.urls import reverse


@pytest.mark.django_db
def test_index_view(client):
    """
    Teste la vue index de l'application lettings.
    Vérifie que la réponse HTTP est 200, que le bon template est utilisé,
    et que le contexte contient une liste de lettings.
    """

    url = reverse('lettings:index')
    response = client.get(url)
    assert response.status_code == 200
    assert 'lettings/index.html' in [element.name for element in response.templates]
    assert 'lettings_list' in response.context


@pytest.mark.django_db
def test_letting_view(client, letting):
    """
    Teste la vue letting de l'application lettings.

    Vérifie que la réponse HTTP est 200 pour un letting_id valide,
    que le bon template est utilisé, et que le contexte contient
    les détails du letting spécifié.

    Teste également que la vue renvoie une réponse 404 pour un letting_id invalide.
    """

    url = reverse('lettings:letting', args=[letting.id])
    response = client.get(url)
    assert response.status_code == 200
    assert 'lettings/letting.html' in [element.name for element in response.templates]
    assert response.context['title'] == letting.title
    assert response.context['address'] == letting.address

    # Test pour un letting_id invalide
    invalid_url = reverse('lettings:letting', args=[999])
    response = client.get(invalid_url)
    assert response.status_code == 404
