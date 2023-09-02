from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import LivrosForm, CategoriaForm
from .models import Livro, Categorias


def home(request):
    return render(request, 'livros/index.html')


def create_books(request):
    if request.method == 'POST':
        form = LivrosForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Livro cadastrado com sucesso!!')
            return redirect('/create_books/')
    else:
        form = LivrosForm

    return render(request, 'livros/create_book.html', {'form': form})


def list_books(request):
    livro = Livro.objects.all()
    return render(request, 'livros/list_books.html', {'livro': livro})


def view_book(request, livro_id):
    livro = get_object_or_404(Livro, pk=livro_id)
    return render(request, 'livros/views_books.html', {'livro': livro})


def edit_book(request, livro_id):
    livro = get_object_or_404(Livro, pk=livro_id)
    if request.method == 'POST':
        form = LivrosForm(request.POST, instance=livro)
        if form.is_valid():
            form.save()
            return redirect('/books/')
    else:
        form = LivrosForm(instance=livro)

    return render(request, 'livros/edit_book.html', {'form': form})


def delete_book(request, livro_id):
    livro = get_object_or_404(Livro, pk=livro_id)
    if request.method == 'POST':
        livro.delete()
        return redirect('/list_books/')
    return render(request, 'livros/delete_book.html', {'livro': livro})


def create_categories(request):
    if request.method == 'POST':
        categoria = request.POST.get('categoria')
        cadastro = Categorias(categoria=categoria)
        cadastro.save()
        return redirect('/create_books/')








