from django.urls import path

from . import views

app_name = 'item'

urlpatterns = [
    path('nowySprzet/', views.nowySprzet, name="nowySprzet"),
    path('nowyKlient/', views.nowyKlient, name="nowyKlient"),
    path('noweWypozyczenie/', views.noweWypozyczenie, name="noweWypozyczenie"),
    path('nowyPakiet/', views.nowyPakiet, name="nowyPakiet"),
    path('sprzet/<int:pk>/', views.sprzet_szczegol, name="sprzet_szczegol"),
    path('klient/<int:pk>/', views.klient_szczegol, name="klient_szczegol"),
    path('wypozyczenie/<int:pk>/', views.wypozyczenie_szczegol, name="wypozyczenie_szczegol"),
]