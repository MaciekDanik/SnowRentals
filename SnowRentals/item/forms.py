from django import forms

from .models import Pracownik, Pakiet, Sprzet, Klient, Wypozyczenie

INPUT_CLASSES = 'w-1/6 py-3 px-4 rounded-xl border'

class NowySprzetForm(forms.ModelForm):
    class Meta:
        model = Sprzet
        fields = ('rodzaj', 'dlugosc', 'marka', 'stan', 'cena',)

        widgets = {
            'rodzaj': forms.Select(attrs={
                'class': INPUT_CLASSES
            }),
            'dlugosc': forms.NumberInput(attrs={
                'class': INPUT_CLASSES
            }),
            'marka': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'stan': forms.Select(attrs={
                'class': INPUT_CLASSES
            }),
            'cena': forms.NumberInput(attrs={
                'class': INPUT_CLASSES
            })
        }


class NowyKlientForm(forms.ModelForm):
    class Meta:
        model = Klient
        fields = ('imie', 'nazwisko', 'PESEL', 'miasto', 'ulica_nrDomu', 'kod_pocztowy', 'nr_telefonu',)


        widgets = {
            'imie': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'nazwisko': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'PESEL': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'miasto': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'ulica_nrDomu': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'kod_pocztowy': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'nr_telefonu': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            })
        }

class NoweWypozyczenieForm(forms.ModelForm):
    class Meta:
        model = Wypozyczenie
        fields = ('klient', 'od', 'do',)

        widgets = {
            'klient': forms.Select(attrs={
                'class': INPUT_CLASSES
            }),
            'od': forms.DateTimeInput(attrs={
                'class': INPUT_CLASSES
            }),
            'do': forms.DateTimeInput(attrs={
                'class': INPUT_CLASSES
            }),
        }

class NowyPakietForm(forms.ModelForm):
    class Meta:
        model = Pakiet
        fields = ('sprzet', 'wypozyczenie',)

        widgets = {
            'sprzet': forms.Select(attrs={
                'class': INPUT_CLASSES
            }),
            'wypozyczenie': forms.Select(attrs={
                'class': INPUT_CLASSES
            })
        }