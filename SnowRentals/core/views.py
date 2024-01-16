from django.shortcuts import render, redirect, get_object_or_404

from item.models import Klient, Sprzet, Wypozyczenie, Utarg, Pakiet, BOOL

from .forms import SignupForm
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, 'core/index.html')

@login_required()
def sprzet(request):
    items = Sprzet.objects.all()
    return render(request, 'core/sprzet.html',{
        'items': items,
    })

@login_required()
def klient(request):
    items = Klient.objects.all()
    return render(request, 'core/klient.html',{
        'items':items,
    })

@login_required()
def wypozyczenie(request):
    TAK = get_object_or_404(BOOL, pk=1)
    NIE = get_object_or_404(BOOL, pk=2)

    items = Wypozyczenie.objects.all().filter(zaplacone=NIE)
    oddane = Wypozyczenie.objects.all().filter(zaplacone=TAK)
    return render(request, 'core/wypozyczenie.html',{
        'items': items,
        'oddane': oddane,
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

def utarg(request):
    item = Utarg.objects.all()

    return render(request, 'core/utarg.html',{
        'item': item,
    })

def logout_view(request):
    logout(request)
    return render(request, 'core/index.html')