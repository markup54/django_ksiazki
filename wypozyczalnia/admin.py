from django.contrib import admin

# Register your models here.


from .models import Autor, Ksiazka

admin.site.register(Autor)
admin.site.register(Ksiazka)