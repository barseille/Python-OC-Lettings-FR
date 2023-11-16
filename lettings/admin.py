from django.contrib import admin

from .models import Letting
from .models import Address

# l'administration Django pour le modèle Letting
admin.site.register(Letting)

# l'administration Django pour le modèle Address
admin.site.register(Address)
