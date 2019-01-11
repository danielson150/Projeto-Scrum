from django.contrib import admin
from core import models

# Personalização do site admin
class ConfeiteiroAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'login', 'foto_perfil', 'email', 'estado', 'cidade')
    list_filter = ['estado', 'cidade']
    search_fields = ['nome', 'login', 'email']
    fieldsets = [
        ('Dados pessoais', {'fields': ['nome', 'login', 'senha', 'email']}),
        ('Imagens descritivas', {'fields': ['foto_perfil', 'foto_capa']}),
        (None, {'fields': ['descricao']}),
        ('Localização', {'fields': ['estado', 'cidade', 'endereco']}),
    ]

class ClienteAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'login')
    search_fields = ['nome', 'login']
    fieldsets = [
        ('Dados pessoais', {'fields': ['nome', 'login', 'Senha']}),
    ]

class PostagemAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'descricao', 'imagem')
    list_filter = ['confeitero']
    search_fields = ['confeitero']

class ClientePublicacaoAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'descricao', 'finalizado')
    list_filter = ['finalizado']
    fieldsets = [
        ('Dados da publicação', {'fields': ['titulo', 'descricao']}),
        ('Imagens descritivas', {'fields': ['imagem']}),
        (None, {'fields': ['finalizado']}),
        ('Solicitante', {'fields': ['cliente']}),
    ]

class ContatoConfeiteiroAdmin(admin.ModelAdmin):
    list_display = ('id', 'numero', 'whatsapp', 'confeitero')
    list_filter = ['whatsapp', 'confeitero']
    search_fields = ['numero']

class ContatoClienteAdmin(admin.ModelAdmin):
    list_display = ('id', 'numero', 'whatsapp', 'cliente')
    list_filter = ['whatsapp', 'cliente']
    search_fields = ['numero']

class AvaliacaoAdmin(admin.ModelAdmin):
    list_display = ('id', 'descricao', 'nota', 'cliente', 'confeitero')
    list_filter = ['cliente', 'confeitero']
    search_fields = ['descricao']
    fieldsets = [
        ('Dados da avalizacao', {'fields': ['descricao', 'nota']}),
        ('Avalição de: ', {'fields': ['cliente']}),
        ('Para: ', {'fields': ['confeitero']}),
    ]

# Register your models here.
admin.site.register(models.Confeiteiro, ConfeiteiroAdmin)
admin.site.register(models.Cliente, ClienteAdmin)
admin.site.register(models.Postagem, PostagemAdmin)
admin.site.register(models.ClientePublicacao, ClientePublicacaoAdmin)
admin.site.register(models.ContatoConfeiteiro, ContatoConfeiteiroAdmin)
admin.site.register(models.ContatoCliente, ContatoClienteAdmin)
admin.site.register(models.Avaliacao, AvaliacaoAdmin)