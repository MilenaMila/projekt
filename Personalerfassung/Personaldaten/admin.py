from django.contrib import admin
from .models import Mitarbeiter, Kinder, Vertragstabelle, Vordienstzeiten # Neu

admin.site.register(Mitarbeiter)
admin.site.register(Kinder)
admin.site.register(Vertragstabelle)
admin.site.register(Vordienstzeiten)

