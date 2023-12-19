from django.contrib import admin

from .models import Pakiet, Pracownik, Sprzet, Klient, Wypozyczenie, Utarg
from .models import Kategoria, Stan

admin.site.register(Pakiet)
admin.site.register(Pracownik)
admin.site.register(Sprzet)
admin.site.register(Klient)
admin.site.register(Wypozyczenie)
admin.site.register(Utarg)
admin.site.register(Kategoria)
admin.site.register(Stan)

