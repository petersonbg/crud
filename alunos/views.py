from django.shortcuts import render, redirect, get_object_or_404
from .forms import FormEndereco, FormAluno
from .models import Aluno, Endereco


def create_student(request):
    if request.method == 'POST':
        form_aluno = FormAluno(request.POST)
        form_endereco = FormEndereco(request.POST)
        if form_aluno.is_valid() and form_endereco.is_valid():
            endereco = form_endereco.save()
            aluno = form_aluno.save(commit=False)
            aluno.endereco = endereco
            aluno.save()
            return redirect('/alunos/list_student')
    else:
        form_aluno = FormAluno
        form_endereco = FormEndereco
    return render(request, 'alunos/create_student.html', {'form_aluno': form_aluno,
                                                          'form_endereco': form_endereco})

def list_student(request):
    aluno = Aluno.objects.all()
    return render(request, 'alunos/list_student.html', {'aluno': aluno})

def view_student(request, aluno_id):
    aluno = get_object_or_404(Aluno, pk=aluno_id)
    return render(request, 'alunos/views_student.html',{'aluno': aluno})
