from multiprocessing import context
from django.shortcuts import render, redirect
from .models import Reserva
from basedailym8.models import Reserva
from .forms import ReservaForm





def home(request):
    context = {'reserva': reserva}
    return render(request, 'home.html', context)

def reserva(request):
    reservas = Reserva.objects.all()
    context = {'reservas': reservas}
    return render(request, 'reservas.html', context)
   

def reservasingle(request):
    return render(request, 'reserva-single.html')
    

def estabelecimento(request):
    return render(request, 'estabelecimento.html')

def estacionamento(request):
    return render(request, 'estacionamento.html')

def Praia(request):
    return render(request, 'Praia.html')


def createReserva(request):
    form = ReservaForm()

    if request.method == 'POST':
        form= ReservaForm(request.POST) 
        if form.is_valid():
            form.save()
            return redirect('create-reserva')

    context = {'form': form}
    return render(request, 'crud.html', context)

def updateReserva(request,pk):
    reserva = Reserva.objects.get(id=pk)
    form = ReservaForm(instance=Reserva)

    if request.method == 'POST':
        form= ReservaForm(request.POST) 
        if form.is_valid():
            form.save()
            return redirect('create-reserva')

    context = {'form': form}
    return render(request, 'crud.html', context)



