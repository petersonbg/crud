# Generated by Django 4.2.4 on 2023-08-28 04:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('alunos', '0004_alter_aluno_endereco'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aluno',
            name='endereco',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='alunos.endereco'),
        ),
    ]
