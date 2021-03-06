# Generated by Django 3.2.13 on 2022-05-16 19:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_alter_despesa_veiculo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='registrosaida',
            name='veiculo',
        ),
        migrations.AddField(
            model_name='registrosaida',
            name='destino',
            field=models.CharField(default='Teresina', max_length=100),
        ),
        migrations.AddField(
            model_name='registrosaida',
            name='hodometro_inicial',
            field=models.IntegerField(default=2),
        ),
        migrations.AddField(
            model_name='registrosaida',
            name='placa',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='veiculo_registro', to='core.veiculo', verbose_name='Placa'),
        ),
    ]
