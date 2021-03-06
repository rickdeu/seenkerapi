# Generated by Django 4.0.3 on 2022-03-19 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_product_name_product_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Nome')),
                ('phone', models.CharField(max_length=200, verbose_name='Telefone')),
                ('email', models.EmailField(max_length=200, verbose_name='Email')),
                ('description', models.TextField(max_length=500, verbose_name='Descricao')),
                ('address', models.CharField(max_length=200, verbose_name='Endereco')),
                ('image', models.ImageField(upload_to='store/%Y/%m/%d', verbose_name='Imagem')),
                ('open', models.TimeField(verbose_name='Abertura')),
                ('close', models.TimeField(verbose_name='Fecho')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Loja',
                'verbose_name_plural': 'Lojas',
                'db_table': 'store',
                'ordering': ['id'],
            },
        ),
    ]
