from django.shortcuts import render, redirect, get_object_or_404
from .forms import FormAluguel
from .models import Aluguel, Livro


def create_alugel(request):
    if request.method == 'POST':
        form = FormAluguel(request.POST)
        if form.is_valid():
            form.save()
            return redirect('create_aluguel')
    else:
        form = FormAluguel
    return render(request, 'alugar/create_aluguel.html', {'form': form})


def list_alugueis(request):
    alugueis = Aluguel.objects.all()
    return render(request, 'alugar/list_alugueis.html', {'alugueis': alugueis})


def view_aluguel(request, aluguel_id):
    alugueis = get_object_or_404(Aluguel, pk=aluguel_id)
    livros_all = alugueis.livro.all()
    return render(request, 'alugar/view_aluguel.html', {'alugueis': alugueis, 'livros_all':livros_all})
