from django.contrib import admin
from django.urls import path, include

from core.views import sprzet, klient, wypozyczenie

urlpatterns = [
    path('', include('core.urls')),
    path('items/', include('item.urls')),
    path('sprzet/', sprzet, name='sprzet'),
    path('klient/', klient, name='klient'),
    path('wypozyczenie/', wypozyczenie, name='wypozyczenie'),
    path('admin/', admin.site.urls),
]
