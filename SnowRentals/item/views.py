import numpy as np
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.db import transaction

from .models import Sprzet, Klient, Wypozyczenie, Pakiet, BOOL
from .forms import NowySprzetForm, NowyKlientForm, NoweWypozyczenieForm, NowyPakietForm, EdytujKlientForm, EdytujWypozyczenieForm, EdytujSprzetForm

def sprzet_szczegol(request, pk):  #szczegóły sprzętu
    item = get_object_or_404(Sprzet, pk=pk)

    if str(item.stan) == "Bardzo dobry":
        item.cena = np.floor(item.cena * 1)
    if str(item.stan) == "Dobry":
        item.cena = np.floor(item.cena * 0.9)
    elif str(item.stan) == "Jeszcze sprawny":
        item.cena = np.floor(item.cena * 0.85)
    elif str(item.stan) == "Nie sprawny":
        item.cena = np.floor(item.cena * 0.7)

    return render(request, 'item/sprzet_szczegol.html',{
        'item': item
    })

def klient_szczegol(request, pk):  #szczegóły klientów
    item = get_object_or_404(Klient, pk=pk)

    return render(request, 'item/klient_szczegol.html',{
        'item': item
    })

def wypozyczenie_szczegol(request, pk):  #szczegóły wypozyczenia
    item = get_object_or_404(Wypozyczenie, pk=pk)
    pakiet = Pakiet.objects.filter(wypozyczenie=item.pk)

    return render(request, 'item/wypozyczenie_szczegol.html',{
        'item': item,
        'pakiet': pakiet
    })

def pracownik_szczegol(request, pk):  #szczegóły sprzętu
    pracownik = get_object_or_404(Klient, pk=pk)

    return render(request, 'item/pracownik_szczegol.html',{
        'pracownik': pracownik
    })

@login_required()
def nowySprzet(request):
    if request.method == 'POST':
        form=NowySprzetForm(request.POST)

        if form.is_valid():
            item = form.save(commit=False) #do wypożyczenia
            #item.arg = request.user
            #item.save()
            item.save()

            return redirect('item:sprzet_szczegol', pk=item.id)

    form = NowySprzetForm()

    return render(request, 'item/form.html',{
        'form': form,
        'title': 'Nowy sprzęt',
    })

@login_required()
def edytuj_sprzet(request, pk):
    item = get_object_or_404(Sprzet, pk=pk)

    if request.method == 'POST':
        form=EdytujSprzetForm(request.POST, instance=item)

        if form.is_valid():
            form.save()

            return redirect('item:sprzet_szczegol', pk=item.id)

    form = EdytujSprzetForm(instance=item)

    return render(request, 'item/form.html',{
        'form': form,
        'title': 'Edytuj sprzęt',
    })

@login_required()
@transaction.atomic()
def noweWypozyczenie(request):
    if request.method == 'POST':
        form = NoweWypozyczenieForm(request.POST)

        if form.is_valid():
            item = form.save(commit=False)
            item.pracownik = request.user
            item.save()

            return redirect('item:wypozyczenie_szczegol', pk=item.id)
        #nowyPakiet(request, item.id):
        #     get item from TABLE id=id
        #     form for Sprzet
        #     pakiet -> wypo_id = item.id

    form = NoweWypozyczenieForm()

    return render(request, 'item/form.html',{
        'form': form,
        'title': 'Nowe wypożyczenie',
    })

@login_required()
def edytuj_wypozyczenie(request, pk):

    item = get_object_or_404(Wypozyczenie, pk=pk)
    if request.method == 'POST':
        form = EdytujWypozyczenieForm(request.POST, instance=item)

        if form.is_valid():
            TAK = get_object_or_404(BOOL, pk=1)
            NIE = get_object_or_404(BOOL, pk=2)
            editedItem = form.save(commit=False)
            if editedItem.zaplacone == TAK:
                pakiet = Pakiet.objects.filter(wypozyczenie=item.id)

                for x in pakiet:
                    sprzet_id = x.sprzet.id
                    sprzet = get_object_or_404(Sprzet, pk=sprzet_id)
                    sprzet.wypozyczone = NIE
                    sprzet.save()

                editedItem.save()
                return redirect('item:wypozyczenie_szczegol', pk=item.id)
            elif editedItem.zaplacone == NIE:
                form.save()
                return redirect('item:wypozyczenie_szczegol', pk=item.id)

    form = EdytujWypozyczenieForm(instance=item)

    return render(request, 'item/form.html',{
        'form': form,
        'title': 'Edytuj wypożyczenie',
    })

@login_required()
def nowyKlient(request):
    if request.method == 'POST':
        form = NowyKlientForm(request.POST)

        if form.is_valid():
            item = form.save(commit=False)
            item.save()

            return redirect('item:klient_szczegol', pk=item.id)

    form = NowyKlientForm()

    return render(request, 'item/form.html',{
        'form': form,
        'title': 'Nowy klient',
    })

@login_required()
def edytuj_klient(request, pk):
    item = get_object_or_404(Klient, pk=pk)

    if request.method == 'POST':
        form = EdytujKlientForm(request.POST, instance=item)

        if form.is_valid():
            form.save()

            return redirect('item:klient_szczegol', pk=item.id)

    form = EdytujKlientForm(instance=item)

    return render(request, 'item/form.html',{
        'form': form,
        'title': 'Edytuj klient',
    })

@login_required()
@transaction.atomic()
def nowyPakiet(request):#, pk):
    if request.method == 'POST':
        form = NowyPakietForm(request.POST)

        if form.is_valid():
            item = form.save(commit=False)
            klucz = item.wypozyczenie.id
            #sprzet = item.sprzet
            sprzet_id = item.sprzet.id

            TAK = get_object_or_404(BOOL, pk=1)
            NIE = get_object_or_404(BOOL, pk=2)
            sprzet = get_object_or_404(Sprzet, pk=sprzet_id)

            if sprzet.wypozyczone == NIE:
                #item.wypozyczenie = get_object_or_404(Wypozyczenie, pk=pk)
                sprzet.wypozyczone = TAK

                item.save()
                sprzet.save()

                return redirect('item:wypozyczenie_szczegol', pk=klucz)
            else:
                return redirect('item:wypozyczenie_szczegol', pk=klucz) #tutaj może dorobię stronę

    form = NowyPakietForm()

    return render(request, 'item/form.html', {
        'form': form,
        'title': 'Pakiet',
    })

@login_required
def delete(request, pk):
    item = get_object_or_404(Sprzet, pk=pk)
    item.delete()

    return redirect('core:index')