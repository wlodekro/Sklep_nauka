from django.contrib import admin

# Register your models here.
from .models import Produkty, Producent, Kategoria

admin.site.register(Produkty)
admin.site.register(Producent)
admin.site.register(Kategoria)
