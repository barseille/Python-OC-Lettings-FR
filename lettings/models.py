from django.db import models
from django.core.validators import MaxValueValidator, MinLengthValidator


class Address(models.Model):
    """
    Représente une adresse physique associée à un bien immobilier.

    Champs :
    - number : Numéro de l'adresse
    - street : Nom de la rue
    - city : Nom de la ville
    - state : Région
    - zip_code : Code postal
    - country_iso_code : Pays
    """
    number = models.PositiveIntegerField(validators=[MaxValueValidator(9999)])
    street = models.CharField(max_length=64)
    city = models.CharField(max_length=64)
    state = models.CharField(max_length=2, validators=[MinLengthValidator(2)])
    zip_code = models.PositiveIntegerField(validators=[MaxValueValidator(99999)])
    country_iso_code = models.CharField(max_length=3, validators=[MinLengthValidator(3)])

    def __str__(self):
        """
        Retourne une représentation en chaîne de caractères de l'adresse.
        """
        return f'{self.number} {self.street}'

    class Meta:
        verbose_name_plural = "Addresses"


class Letting(models.Model):
    """
    Représente un bien immobilier à louer.

    Champs :
    - title : Nom du bien immobilier.
    - address : Lien vers l'objet Address associé.
    """
    title = models.CharField(max_length=256)
    address = models.OneToOneField(Address, on_delete=models.CASCADE)

    def __str__(self):
        """
        Retourne le nom du bien immobilier.
        """
        return self.title
