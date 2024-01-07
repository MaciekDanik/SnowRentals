from django.urls import path

from . import views

app_name = 'item'

urlpatterns = [
    path('nowySprzet/', views.nowySprzet, name="nowySprzet"),
    path('nowyKlient/', views.nowyKlient, name="nowyKlient"),
    path('noweWypozyczenie/', views.noweWypozyczenie, name="noweWypozyczenie"),
    path('nowyPakiet/<int:pk>', views.nowyPakiet, name="nowyPakiet"),
    path('sprzet/<int:pk>/', views.sprzet_szczegol, name="sprzet_szczegol"),
    path('sprzet/<int:pk>/delete/', views.delete, name="delete"),
    path('klient/<int:pk>/', views.klient_szczegol, name="klient_szczegol"),
    path('wypozyczenie/<int:pk>/', views.wypozyczenie_szczegol, name="wypozyczenie_szczegol"),
    path('klient/<int:pk>/edytuj_klient/', views.edytuj_klient, name="edytuj_klient"),
    path('wypozyczenie/<int:pk>/edytuj_wypozyczenie/', views.edytuj_wypozyczenie, name="edytuj_wypozyczenie"),
    path('sprzet/<int:pk>/edytuj_sprzet/', views.edytuj_sprzet, name="edytuj_sprzet"),
]