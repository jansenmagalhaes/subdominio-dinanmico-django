# Generated by Django 5.0.1 on 2024-01-15 02:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0002_alter_usuario_organizacao'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='sessao_app',
            field=models.CharField(blank=True, max_length=40),
        ),
        migrations.AddField(
            model_name='usuario',
            name='sessao_site',
            field=models.CharField(blank=True, max_length=40),
        ),
    ]
