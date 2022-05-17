from django.shortcuts import render

from . models import Veiculo

# Create your views here.


def home(request):
    return render(request, 'index.html')

def lista_veiculos(request):
    veiculos = Veiculo.objects.all()
    context = {
        'veiculos': veiculos
    }
    return render(request, 'list-veiculos.html', context)


def registrar_saida(request):
    placa = 'NIX 4081'
    veiculo = Veiculo.objects.filter(placa__icontains=placa)
    if veiculo:
        for veiculo in veiculo:
            if veiculo.status == "Disponivel":
                print('Faça isso')

            elif veiculo.status == "Indisponível":
                print("Veiculo Indisponivel")

    else:
        print('Placa invalida')
    
    return render(request, 'reg-saida.html')


def registrar_entrada(request):
    return render(request, 'reg-entrada.html')

