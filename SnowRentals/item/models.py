from  django.contrib.auth.models import User
from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

def wiekszeOdZera(wartosc):
    if wartosc < 0:
        raise ValidationError(
            _("%(wartosc)s jest ujemna, spróbuj ponownie."),
            params = {"wartosc": wartosc},)

def Isbool(wartosc):
    if (wartosc != 0) and (wartosc != 1):
        raise ValidationError(
            _("%(wartosc)s jest nieprawidlowa"),
            params = {"wartosc": wartosc},)

def PESEL_validation(wartosc):
    if (len(wartosc) != 11):
        raise ValidationError(
            _("%(wartosc)s ma nie odpowiednią długość, spróbuj ponownie."),
            params={"wartosc": wartosc}, )

def TEL_validation(wartosc):
    if (len(wartosc) != 9):
        raise ValidationError(
            _("%(wartosc)s ma nie odpowiednią długość, spróbuj ponownie."),
            params={"wartosc": wartosc}, )

def KOD_validation(wartosc):
    if (len(wartosc) != 6):
        raise ValidationError(
            _("%(wartosc)s ma nie odpowiednią długość, spróbuj ponownie."),
            params={"wartosc": wartosc}, )


class Pracownik(models.Model):
    imie = models.CharField(max_length=40)
    nazwisko = models.CharField(max_length=40)

    class Meta:
        ordering=('imie',)
        verbose_name_plural = 'Pracownicy'

    def __str__(self):
        return self.imie + " " + self.nazwisko

class BOOL(models.Model):
    TYPE = models.CharField(max_length=3)

    class Meta:
        ordering=('TYPE',)
        verbose_name_plural = 'Typy'

    def __str__(self):
        return self.TYPE


class Klient(models.Model):
    imie = models.CharField(max_length=40)
    nazwisko = models.CharField(max_length=40)
    PESEL = models.CharField(max_length=11, unique=True, validators=[PESEL_validation])
    miasto = models.CharField(max_length=50, null=False, default="---")
    ulica_nrDomu = models.CharField(max_length=50, null=False, default="---")
    kod_pocztowy = models.CharField(max_length=6, validators=[KOD_validation])
    nr_telefonu = models.CharField(max_length=9, unique=True, validators=[TEL_validation])

    class Meta:
        ordering=('imie',)
        verbose_name_plural = 'Klienci'

    def __str__(self):
        return self.imie+" "+self.nazwisko

class Utarg(models.Model):
    data = models.DateField("Utarg z dnia: ") #, auto_now_add=True
    kwota = models.FloatField(validators=[wiekszeOdZera],default=0)

    class Meta:
        ordering=('data',)
        verbose_name_plural = 'Utarg'

    def __str__(self):
        return "Utarg: " + str(self.data)

class Wypozyczenie(models.Model):
    pracownik = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    klient = models.ForeignKey(Klient, related_name='items', null=True, on_delete=models.SET_NULL)
    od = models.DateField("Wypozyczone: ") #, auto_now_add=True
    do = models.DateField("Zwrocone: ")
    zaplacone = models.ForeignKey(BOOL, null=True, on_delete=models.SET_NULL)

    class Meta:
        verbose_name_plural = 'Wypożyczenia'

    def __str__(self):
        return str(self.klient)+" "+str(self.od)+" "+str(self.zaplacone)


class Kategoria(models.Model):
    kategoria = models.CharField(max_length=40)

    class Meta:
        ordering=('kategoria',)
        verbose_name_plural = 'Kategorie'

    def __str__(self):
        return self.kategoria

class Stan(models.Model):
    stan = models.CharField(max_length=20)

    class Meta:
        ordering=('stan',)
        verbose_name_plural = 'Stany'

    def __str__(self):
        return self.stan


class Sprzet(models.Model):
    rodzaj = models.ForeignKey(Kategoria, on_delete=models.CASCADE)
    dlugosc = models.IntegerField(validators=[wiekszeOdZera], null=False, default=0)
    marka = models.CharField(max_length=40)
    stan = models.ForeignKey(Stan, on_delete=models.CASCADE)
    cena = models.IntegerField(validators=[wiekszeOdZera], default=30)
    wypozyczone = models.ForeignKey(BOOL, null=True, on_delete=models.SET_NULL)

    class Meta:
        ordering = ('rodzaj',)
        verbose_name_plural = 'Lista sprzętu'

    def __str__(self):
        return str(self.rodzaj) + " " + str(self.dlugosc) + " " + str(self.wypozyczone)


class Pakiet(models.Model):
    sprzet = models.ForeignKey(Sprzet, null=True, on_delete=models.SET_NULL)
    #sprzet1 = models.ManyToManyField()
    wypozyczenie = models.ForeignKey(Wypozyczenie, null=True, on_delete=models.SET_NULL)

    class Meta:
        verbose_name_plural = 'Pakiety'

    def __str__(self):
        return str(self.wypozyczenie)