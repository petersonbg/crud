# Generated by Django 4.2.4 on 2023-08-28 03:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alunos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='aluno',
            name='email',
            field=models.EmailField(blank=True, max_length=100, null=True),
        ),
    ]