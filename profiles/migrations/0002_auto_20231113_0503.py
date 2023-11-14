from django.db import migrations

def transfer_profiles_data(apps, schema_editor):
    """
    Transfère les données de l'ancien modèle Profile du module 'oc_lettings_site'
    vers le nouveau modèle Profile dans le module 'profiles'.

    Cette fonction est utilisée comme une opération de migration pour préserver les données
    lors de la transition vers une nouvelle structure de base de données modulaire.
    """
    
    # Récupération de l'ancien modèle Profile à partir de l'application 'oc_lettings_site'
    OldProfileModel = apps.get_model('oc_lettings_site', 'Profile')
    
    # Récupération du nouveau modèle Profile à partir de l'application 'profiles'
    NewProfileModel = apps.get_model('profiles', 'Profile')
    
    # Récupération du modèle User pour la relation OneToOne avec Profile
    User = apps.get_model('auth', 'User')

    # Transfert des données de l'ancien modèle vers le nouveau modèle
    for old_profile in OldProfileModel.objects.all():
        
        # Récupération de l'utilisateur associé à l'ancien profil
        user = User.objects.get(id=old_profile.user_id)
        
        # Création d'un nouveau profil avec les données de l'ancien profil
        NewProfileModel.objects.create(
            user=user,
            favorite_city=old_profile.favorite_city,
        )

def reverse_profiles_data(apps, schema_editor):
    """
    Annule la migration des données de profil en supprimant toutes les entrées
    du nouveau modèle Profile dans le module 'profiles'.

    Cette fonction est appelée comme une opération inverse dans le cadre de la migration
    pour permettre le retour à un état antérieur si nécessaire.
    """
    
    # Suppression de toutes les données du nouveau modèle Profile pour annuler la migration
    NewProfileModel = apps.get_model('profiles', 'Profile')
    NewProfileModel.objects.all().delete()

class Migration(migrations.Migration):
    """
    Définit une migration pour transférer les données du modèle Profile
    de l'application 'oc_lettings_site' à l'application 'profiles'.

    Cette migration s'appuie sur les fonctions 'transfer_profiles_data' et 'reverse_profiles_data'
    pour appliquer et annuler les changements respectivement.
    """

    dependencies = [
        # Dépendance sur la première migration initiale de l'application 'profiles'
        ('profiles', '0001_initial'),
    ]

    operations = [
        # Opérations de migration pour transférer et annuler les données
        migrations.RunPython(transfer_profiles_data, reverse_profiles_data),
    ]
