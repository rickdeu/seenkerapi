from email.headerregistry import Address
from django.db import models
from datetime import datetime


class Banner(models.Model):
    name = models.CharField(
        max_length=150, verbose_name='Nome', blank=False, null=False)
    description = models.TextField(
        max_length=250, verbose_name='Descricao', null=True, blank=True)
    image = models.ImageField(
        upload_to='banner/%Y/%m/%d', null=False, blank=False)
    isActive = models.BooleanField(default=False, verbose_name='Activo')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Banner'
        verbose_name_plural = 'Banners'
        db_table = 'banner'
        ordering = ['id']


class Category(models.Model):
    name = models.CharField(max_length=150, verbose_name='Nome', unique=True)
    description = models.TextField(
        max_length=250, verbose_name='Descricao', null=True, blank=True)
    image = models.ImageField(
        upload_to='category/%Y/%m/%d', null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        db_table = 'category'
        ordering = ['id']


class Product(models.Model):
    category = models.ForeignKey(
        Category,
        related_name='products',
        on_delete=models.CASCADE,
        verbose_name="Categoria",
    )
    name = models.CharField(
        max_length=200,
        # db_index=True,
        verbose_name="Nome")
    slug = models.SlugField(
        max_length=200,
        # db_index=True
    )
    description = models.TextField(
        blank=True)

    image = models.ImageField(
        upload_to='products/%Y/%m/%d',
        blank=True,
        verbose_name="Imagem"
    )

    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="Price",
    )
    avaliable = models.BooleanField(
        default=True,
        verbose_name='Disponivel'
    )
    isEmphasi = models.BooleanField(
        default=False,
        verbose_name='Destaque'
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        db_table = 'product'
        ordering = ['id']


class Store(models.Model):
    name = models.CharField(
        max_length=200,
        verbose_name="Nome")
    phone = models.CharField(
        max_length=200,
        null=True,
        blank=True,
        verbose_name="Telefone")
    email = models.EmailField(
        max_length=200,
        null=True,
        blank=True,
        verbose_name="Email")
    description = models.TextField(
        max_length=500,
        null=True,
        blank=True,
        verbose_name="Descricao")
    address = models.CharField(
        max_length=200,
        null=True,  
        blank=True,
        verbose_name="Endereco")
    lat = models.CharField(verbose_name='Latitude',        null=True,
                           blank=True, max_length=50)
    log = models.CharField(verbose_name='Longitude',        null=True,
                           blank=True, max_length=50)
    image = models.ImageField(
        upload_to='store/%Y/%m/%d',
        verbose_name="Imagem"
    )
    open = models.TimeField(verbose_name="Abertura",        null=True,
                            blank=True,)
    close = models.TimeField(verbose_name="Fecho",        null=True,
                             blank=True,)
    created_at = models.DateTimeField(
        auto_now_add=True,        null=True,
        blank=True,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Loja'
        verbose_name_plural = 'Lojas'
        db_table = 'store'
        ordering = ['id']
