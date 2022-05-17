from django.urls import path


from . import views


urlpatterns = [ 
    path('', views.home, name="home"),
    path('lista-veiculo/', views.lista_veiculos, name="list-veiculos"),
    path('regitro-saida/', views.registrar_saida, name="reg-saida"),
    path('regitro-entrada/', views.registrar_entrada, name="reg-entrada"),
]
