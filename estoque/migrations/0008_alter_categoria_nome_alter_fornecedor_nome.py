# Generated by Django 5.0.6 on 2024-05-23 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estoque', '0007_produto_observacao_saida_observacao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categoria',
            name='nome',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='fornecedor',
            name='nome',
            field=models.CharField(max_length=100),
        ),
    ]