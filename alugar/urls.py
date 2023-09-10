from django.urls import path
from .views import *

app_name = 'alugar'

urlpatterns = [
    path('create_aluguel/', create_alugel, name='create_aluguel'),
    path('list_alugueis/', list_alugueis, name='list_alugueis'),
    path('view_aluguel/<int:aluguel_id>/', view_aluguel, name='view_aluguel')
]