from django.db import migrations


def transfer_lettings_data(apps, schema_editor):
    """
    Transfère les données de l'ancien modèle Letting et Address du module 'oc_lettings_site'
    vers les nouveaux modèles Letting et Address dans le module 'lettings'.

    Cette fonction est utilisée comme une opération de migration pour préserver les données
    lors de la transition vers une nouvelle structure de base de données modulaire.
    """
    
    # Récupération des anciens modèles de données à partir de l'application 'oc_lettings_site'
    OldLettingModel = apps.get_model('oc_lettings_site', 'Letting')
    OldAddressModel = apps.get_model('oc_lettings_site', 'Address')
    
    # Récupération des nouveaux modèles de données à partir de l'application 'lettings'
    NewAddressModel = apps.get_model('lettings', 'Address')
    NewLettingModel = apps.get_model('lettings', 'Letting')

    # Transfert des données de l'ancien modèle vers le nouveau modèle
    for old_letting in OldLettingModel.objects.all():
        
        # Création d'une nouvelle adresse pour chaque letting
        new_address = NewAddressModel.objects.create(
            number=old_letting.address.number,
            street=old_letting.address.street,
            city=old_letting.address.city,
            state=old_letting.address.state,
            zip_code=old_letting.address.zip_code,
            country_iso_code=old_letting.address.country_iso_code,
        )
        
        # Création d'un nouveau letting associé à la nouvelle adresse
        NewLettingModel.objects.create(
            title=old_letting.title,
            address=new_address,
        )


def reverse_lettings_data(apps, schema_editor):
    """
    Annule la migration des données de letting en supprimant toutes les entrées
    des nouveaux modèles Letting et Address dans le module 'lettings'.

    Cette fonction est appelée comme une opération inverse dans le cadre de la migration
    pour permettre le retour à un état antérieur si nécessaire.
    """
     
    # Suppression de toutes les données des nouveaux modèles pour annuler la migration
    NewLettingModel = apps.get_model('lettings', 'Letting')
    NewAddressModel = apps.get_model('lettings', 'Address')
    
    # Suppression des données doit être faite en respectant l'ordre des dépendances
    # Suppression des lettings d'abord, car ils dépendent des adresses
    NewLettingModel.objects.all().delete()
    
    # Ensuite, suppression des adresses
    NewAddressModel.objects.all().delete()


class Migration(migrations.Migration):
    """
    Définit une migration pour transférer les données des modèles Letting et Address
    de l'application 'oc_lettings_site' à l'application 'lettings'.

    Cette migration s'appuie sur les fonctions 'transfer_lettings_data' et 'reverse_lettings_data'
    pour appliquer et annuler les changements respectivement.
    """

    dependencies = [
        # Dépendance sur la première migration initiale de l'application 'lettings'
        ('lettings', '0001_initial'),
    ]

    operations = [
        # Opérations de migration pour transférer et annuler les données
        migrations.RunPython(transfer_lettings_data, reverse_lettings_data),
    ]
