from django.urls import path
from .views import *

app_name = 'alunos'

urlpatterns = [
    path('create_student/', create_student, name='create_student'),
    path('list_student/', list_student, name='list_student'),
    path('view_student/<int:aluno_id>/', view_student, name='view_student')
]