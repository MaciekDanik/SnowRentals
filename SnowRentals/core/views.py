from django.shortcuts import render, redirect

from item.models import Klient, Pracownik, Sprzet, Wypozyczenie, Utarg, Pakiet

from .forms import SignupForm
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, 'core/index.html')

@login_required()
def sprzet(request):
    items = Sprzet.objects.all()
    return render(request, 'core/sprzet.html',{
        'items':items,
    })

@login_required()
def klient(request):
    items = Klient.objects.all()
    return render(request, 'core/klient.html',{
        'items':items,
    })

@login_required()
def wypozyczenie(request):
    items = Wypozyczenie.objects.all()
    return render(request, 'core/wypozyczenie.html',{
        'items':items
    })

def kontakt(request):
    return render(request, 'core/kontakt.html')

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('/login/')
        else:
            form = SignupForm()
    form = SignupForm()

    return render(request, 'core/signup.html',{
        'form': form
    })

def logout_view(request):
    logout(request)
    return render(request, 'core/index.html')