# Generated by Django 2.1.3 on 2018-12-29 16:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Avaliacao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.TextField(max_length=250)),
                ('nota', models.DecimalField(decimal_places=2, max_digits=4)),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('login', models.CharField(max_length=15)),
                ('Senha', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='ClientePublicacao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=50)),
                ('descricao', models.TextField(max_length=250)),
                ('imagem', models.ImageField(blank=True, null=True, upload_to='galeria/postagem/cliente')),
                ('finalizado', models.BooleanField()),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Cliente')),
            ],
        ),
        migrations.CreateModel(
            name='Confeiteiro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('login', models.CharField(max_length=15)),
                ('Senha', models.CharField(max_length=15)),
                ('foto_perfil', models.ImageField(blank=True, null=True, upload_to='galeria/perfil')),
                ('foto_capa', models.ImageField(blank=True, null=True, upload_to='galeria/perfil/capa')),
                ('descricao', models.TextField(max_length=250)),
                ('email', models.CharField(max_length=50)),
                ('estado', models.CharField(max_length=20)),
                ('cidade', models.CharField(max_length=20)),
                ('endereco', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='ContatoCliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.CharField(max_length=15)),
                ('whatsapp', models.BooleanField(default=False)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Cliente')),
            ],
        ),
        migrations.CreateModel(
            name='ContatoConfeiteiro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.CharField(max_length=15)),
                ('whatsapp', models.BooleanField(default=False)),
                ('confeitero', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Confeiteiro')),
            ],
        ),
        migrations.CreateModel(
            name='Postagem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=50)),
                ('descricao', models.TextField(max_length=250)),
                ('imagem', models.ImageField(blank=True, null=True, upload_to='galeria/postagem/confeiteiro')),
                ('confeitero', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Confeiteiro')),
            ],
        ),
        migrations.AddField(
            model_name='avaliacao',
            name='cliente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Cliente'),
        ),
        migrations.AddField(
            model_name='avaliacao',
            name='confeitero',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Confeiteiro'),
        ),
    ]
