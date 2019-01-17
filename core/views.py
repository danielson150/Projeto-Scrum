from django.shortcuts import render, redirect
from core.forms import *
from core.models import *
from django.core.files.storage import FileSystemStorage


# Create your views here.
def home(request):
    # Login
    if request.method == 'POST':
        login = request.POST.get('login')
        senha = request.POST.get('senha')
        if logar(request, login, senha):
            if recuperar_elemento_da_session(request, 'tipo_de_usuario') == 'confeiteiro':
                return redirect('/dashboard')
            else:
                return redirect('/cliente')

    dicionario = {
        'confeiteiros': Confeiteiro.objects.exclude(foto_perfil='').exclude(descricao=''),
        'solicitacoes': ClientePublicacao.objects.exclude(titulo='').exclude(descricao='').exclude(imagem='').filter(finalizado=False),
        'usuario_logado': recuperar_elemento_da_session(request, 'usuario_logado'),
        'tipo_de_usuario': recuperar_elemento_da_session(request, 'tipo_de_usuario')
    }
    return render(request, 'index.html', dicionario)


def cadastrar(request):
    flash_message = ''

    if request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        login = request.POST.get('login')
        senha = request.POST.get('senha')
        repete_senha = request.POST.get('repetesenha')
        tipo_de_usuario = request.POST.get('tipo')

        if tipo_de_usuario == 'confeiteiro':
            resposta_do_cadastro = cadastrar_novo_confeiteiro(nome, email, login, senha, repete_senha)
            if resposta_do_cadastro[0] == True:
                return redirect('/')
            else:
                flash_message = resposta_do_cadastro[1]
        else:
            resposta_do_cadastro = cadastrar_novo_cliente(nome, login, senha, repete_senha)
            if resposta_do_cadastro[0] == True:
                return redirect('/')
            else:
                flash_message = resposta_do_cadastro[1]

    return render(request, 'cadastro.html', {'flash_message': flash_message})


def dashboard(request):
    if not usuario_logado(request, 'confeiteiro'):
        return redirect('/')

    id_do_usuario = recuperar_elemento_da_session(request, 'id_do_usuario')
    dados_para_template = {
        'postagens': Postagem.objects.all(),
        'dados_do_usuario': Confeiteiro.objects.get(id=id_do_usuario),
        'solicitacoes': ClientePublicacao.objects.exclude(titulo='').exclude(descricao='').exclude(imagem='').filter(finalizado=False),
    }
    return render(request, 'profissional.html', dados_para_template)


def nova_postagem(request):
    if not usuario_logado(request, 'confeiteiro'):
        return redirect('/')

    if request.method == 'POST':
        imagem = request.FILES['imagem']
        titulo = request.POST.get('titulo')
        descricao = request.POST.get('descricao')
        preco = request.POST.get('preco')
        tipo = request.POST.get('tipo')
        user_id = recuperar_elemento_da_session(request, 'id_do_usuario')
        # Salvar imagem no servidor
        file_system = FileSystemStorage()
        nome_do_arquivo_salvo = file_system.save(imagem.name, imagem)
        # Salvar nome da imagem no banco de dados
        confeiteiro = selecionar_confeiteiro_por_id(user_id)
        postagem = Postagem(titulo=titulo, imagem=nome_do_arquivo_salvo, descricao=descricao, preco=preco, categoria=tipo, confeitero=confeiteiro)
        postagem.save()

    return redirect('/dashboard/')


def cliente(request):
    if not usuario_logado(request, 'cliente'):
        return redirect('/')
    id_do_usuario = recuperar_elemento_da_session(request, 'id_do_usuario')
    dados_para_template = {
        'postagens': ClientePublicacao.objects.all(),
        'dados_do_usuario': Cliente.objects.get(id=id_do_usuario),
    }
    return render(request, 'cliente.html', dados_para_template)


def nova_solicitacao(request):
    if not usuario_logado(request, 'cliente'):
        return redirect('/')

    if request.method == 'POST':
        imagem = request.FILES['imagem']
        titulo = request.POST.get('titulo')
        descricao = request.POST.get('descricao')
        user_id = recuperar_elemento_da_session(request, 'id_do_usuario')
        # Salvar imagem no servidor
        file_system = FileSystemStorage()
        nome_do_arquivo_salvo = file_system.save(imagem.name, imagem)
        # Salvar nome da imagem no banco de dados
        cliente = selecionar_cliente_por_id(user_id)
        solicitacao = ClientePublicacao(titulo=titulo, descricao=descricao, imagem=nome_do_arquivo_salvo, finalizado=False, cliente=cliente)
        solicitacao.save()

    return redirect('/cliente/')


'''
Funções a partir desta parte são apenas operacionais, o controle das views fica acima
'''


# Funções para a gerencia de confeiteiros
def seleciona_todos_os_confeiteiros_cadastrados():
    return Confeiteiro.objects.all()


def cadastrar_novo_confeiteiro(nome, email, login, senha, senha_repetida):
    if senha != senha_repetida:
        return False, 'Senhas diferentes'
    else:
        if len(nome) == 0 or len(email) == 0 or len(login) == 0 or len(senha) == 0:
            return False, 'Todos os campos são obrigatórios'
        else:
            confeiteiro = Confeiteiro(nome=nome, email=email, login=login, senha=senha)
            confeiteiro.save()
    return True, 'Cadastrado com sucesso!'


def selecionar_confeiteiro_por_id(id):
    return Confeiteiro.objects.get(id=id)


def deletar_confeiteiro_por_id(pk):
    confeiteiro = Confeiteiro.objects.get(pk=pk)
    confeiteiro.delete()


# Funções para a gerencia de clientes
def cadastrar_novo_cliente(nome, login, senha, senha_repetida):
    if senha != senha_repetida:
        return False, 'Senhas diferentes'
    else:
        if len(nome) == 0 or len(login) == 0 or len(senha) == 0:
            return False, 'Todos os campos são obrigatórios'
        else:
            confeiteiro = Cliente(nome=nome, login=login, Senha=senha)
            confeiteiro.save()
    return True, 'Cadastrado com sucesso!'


def selecionar_cliente_por_id(id):
    return Cliente.objects.get(id=id)


# funções para Controle de sessão
def adiciona_elemento_a_session(request, chave, valor):
    request.session[chave] = valor


def recuperar_elemento_da_session(request, chave):
    return request.session.get(chave, '')


def logar(request, login, senha):
    logado_com_sucesso = False
    tipo_de_usuario = ''
    nome_do_usuario = ''
    id_do_usuario = -1

    if len(Confeiteiro.objects.all().filter(login=login, senha=senha)) == 1:
        confeiteiro = Confeiteiro.objects.all().filter(login=login, senha=senha)
        logado_com_sucesso = True
        tipo_de_usuario = 'confeiteiro'
        id_do_usuario = confeiteiro[0].id
        nome_do_usuario = confeiteiro[0].nome

    elif len(Cliente.objects.all().filter(login=login, Senha=senha)) == 1:
        cliente = Cliente.objects.all().filter(login=login, Senha=senha)
        logado_com_sucesso = True
        tipo_de_usuario = 'cliente'
        id_do_usuario = cliente[0].id
        nome_do_usuario = cliente[0].nome

    if logado_com_sucesso:
        adiciona_elemento_a_session(request, 'usuario_logado', True)
        adiciona_elemento_a_session(request, 'id_do_usuario', id_do_usuario)
        adiciona_elemento_a_session(request, 'login_do_usuario', login)
        adiciona_elemento_a_session(request, 'nome_do_usuario', nome_do_usuario)
        adiciona_elemento_a_session(request, 'tipo_de_usuario', tipo_de_usuario)

    return logado_com_sucesso


def deslogar(request):
    request.session['usuario_logado'] = False
    del request.session['id_do_usuario']
    del request.session['login_do_usuario']
    del request.session['nome_do_usuario']
    del request.session['tipo_de_usuario']
    return redirect('/')


def usuario_logado(request, tipo_de_usuario):
    if not recuperar_elemento_da_session(request, 'usuario_logado'):
        return False
    else:
        if recuperar_elemento_da_session(request, 'tipo_de_usuario') != tipo_de_usuario:
            return False
    return True
