import pytest


@pytest.mark.django_db
def test_profile_model(profile):
    """
    Teste que le modèle Profile est correctement créé et
    que sa représentation en chaîne est correcte.
    """
    assert profile.user.username == 'testuser'
    assert profile.favorite_city == "Paris"
    assert str(profile) == 'testuser'
