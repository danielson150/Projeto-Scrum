from django.db import models

# Create your models here.
class Confeiteiro(models.Model):
    nome = models.CharField(max_length=50)
    login = models.CharField(max_length=15)
    senha = models.CharField(max_length=15)
    foto_perfil = models.ImageField(null=True, blank=True, upload_to='galeria/perfil')
    foto_capa = models.ImageField(null=True, blank=True, upload_to='galeria/perfil/capa')
    descricao = models.TextField(null=True, blank=True, max_length=250)
    email = models.CharField(max_length=50)
    estado = models.CharField(null=True, blank=True, max_length=20)
    cidade = models.CharField(null=True, blank=True, max_length=20)
    endereco = models.CharField(null=True, blank=True, max_length=50)

class ContatoConfeiteiro(models.Model):
    numero = models.CharField(max_length=15)
    whatsapp = models.BooleanField(default=False)
    confeitero = models.ForeignKey(Confeiteiro, on_delete=models.CASCADE)

class Postagem(models.Model):
    CATEGORIA_CHOICES = (
        ('Bolo de Aniversário', 'Bolo de Aniversário'),
        ('Bolo de Casamento', 'Bolo de Casamento'),
        ('Cupcake', 'Cupcake'),
        ('Rocambole', 'Rocambole'),
        ('Bolo de camadas', 'Bolo de camadas'),

    )
    titulo = models.CharField(max_length=50)
    descricao = models.TextField(max_length=250)
    categoria = models.CharField('Categoria', max_length=40, choices=CATEGORIA_CHOICES)
    imagem = models.ImageField(null=True, blank=True, upload_to='galeria/postagem/confeiteiro')
    preco = models.DecimalField('Preço', max_digits=8, decimal_places=2, default=0)
    confeitero = models.ForeignKey(Confeiteiro, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Postagens'
        verbose_name = 'Postagem'


class Cliente(models.Model):
    nome = models.CharField(max_length=50)
    login = models.CharField(max_length=15)
    Senha = models.CharField(max_length=15)

class ContatoCliente(models.Model):
    numero = models.CharField(max_length=15)
    whatsapp = models.BooleanField(default=False)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)

class ClientePublicacao(models.Model):
    titulo = models.CharField(max_length=50)
    descricao = models.TextField(max_length=250)
    imagem = models.ImageField(null=True, blank=True, upload_to='galeria/postagem/cliente')
    finalizado = models.BooleanField()
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Cliente Publicações'
        verbose_name = 'Cliente Publicação'


class Avaliacao(models.Model):
    descricao = models.TextField(max_length=250)
    nota = models.DecimalField(max_digits=4, decimal_places=2)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    confeitero = models.ForeignKey(Confeiteiro, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Avaliações'
        verbose_name = 'Avaliação'

