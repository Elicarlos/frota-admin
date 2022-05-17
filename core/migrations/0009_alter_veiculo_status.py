# Generated by Django 3.2.13 on 2022-05-17 05:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_veiculo_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='veiculo',
            name='status',
            field=models.CharField(choices=[('Disponivel', 'Disponivel'), ('Indisponível', 'Indisponivel'), ('Manutencão', 'Manuntencao')], default=1, max_length=20),
        ),
    ]
