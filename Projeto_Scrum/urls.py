from django.contrib import admin
from django.urls import path
from core import views

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('cadastrar/', views.cadastrar, name='cadastrar'),
    path('login/', views.login, name='login'),
    path('deslogar/', views.deslogar, name='deslogar'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('dashboard/postar/', views.nova_postagem, name='novo_servico'),
    path('dashboard/atualizar/', views.atualizar_dados_do_confeiteiro, name='atualizar_dados_do_confeiteiro'),
    path('dashboard/novocontato/', views.novo_contato_do_confeiteiro, name='novo_contato_confeiteiro'),
    path('cliente/', views.cliente, name='cliente'),
    path('cliente/postar/', views.nova_solicitacao, name='nova_solicitacao'),
    path('cliente/novocontato/', views.novo_contato_do_cliente, name='novo_contato_cliente'),
]


# Função para que o django mostre imagens durante o desenvolvimento
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)