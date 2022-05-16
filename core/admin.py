
from django.contrib import admin
from .models import TipoDespesa, TipoVeiculo, Veiculo, Despesa, RegistroSaida

# Register your models here.
admin.site.register(TipoDespesa)
admin.site.register(TipoVeiculo)
admin.site.register(Veiculo)
admin.site.register(Despesa)
admin.site.register(RegistroSaida)
