from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    """
    Représente le profil d'un utilisateur.

    Champs :
    - user : Lien vers l'instance du modèle User de Django.
             Ce champ établit une relation un-à-un avec le modèle User.

    - favorite_city : Ville préférée de l'utilisateur. Ce champ est facultatif.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favorite_city = models.CharField(max_length=64, blank=True)

    def __str__(self):
        return self.user.username
