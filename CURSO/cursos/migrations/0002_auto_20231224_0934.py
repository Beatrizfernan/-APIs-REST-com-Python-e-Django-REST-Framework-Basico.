# Generated by Django 2.2.9 on 2023-12-24 12:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cursos', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='avaliacao',
            old_name='publicacao',
            new_name='criacao',
        ),
        migrations.RenameField(
            model_name='curso',
            old_name='publicacao',
            new_name='criacao',
        ),
    ]