from django.db import models
from datetime import datetime

from django.forms import model_to_dict
from config.settings import MEDIA_URL, STATIC_URL

# from django.db.models.deletion import CASCADE
from core.erp.choices import gender_choices

# Create your models here.

# class Type(models.Model):
#     name = models.CharField(max_length=150, verbose_name="Nombre")

#     # Metodo str, to string
#     def __str__(self):
#         return self.name

#     # LA clse meta para propiedades
#     db_table = 'tipo'
#     verbose_name = 'Tipo'
#     verbose_name_plural = 'Tipos'
#     ordering = ['id']


# class Category(models.Model):
#     name = models.CharField(max_length=150, verbose_name="Nombre")

#     # Metodo str, to string
#     def __str__(self):
#         return self.name

#     # LA clse meta para propiedades
#     db_table = 'categoria'
#     verbose_name = 'Categoria'
#     verbose_name_plural = 'Categorias'
#     ordering = ['id']



# class Employee(models.Model):
#     # Para relacionar la tabla
#     category = models.ManyToManyField(Category)
#     type = models.ForeignKey(Type, on_delete=models.CASCADE) #models.protect para proteger
#     names = models.CharField(max_length=150, verbose_name="Nombres")
#     dni = models.CharField(max_length=8, verbose_name="DNI"),
#     date_joined = models.DateField(default=datetime.now, verbose_name="Fecha de registro")
#     date_creation = models.DateTimeField(auto_now=True)
#     date_update = models.DateTimeField(auto_now_add=True)
#     age = models.PositiveIntegerField(default=0)
#     salary = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
#     gender = models.CharField(max_length=20, null=True, blank=True)
#     status = models.BooleanField(default=True)
#     avatar = models.ImageField(upload_to='avatar/%Y/%m/%d', null=True, blank=True)
#     cvitae = models.FileField(upload_to='cvitae/%Y/%m/%d', null=True, blank=True)

#     # Metodo str, to string
#     def __str__(self):
#         return self.names

#     # LA clse meta para propiedades
#     db_table = 'empleado'
#     verbose_name = 'Empleado'
#     verbose_name_plural = 'Empleados'
#     ordering = ['id']



class Category(models.Model):
    name = models.CharField(max_length=150, verbose_name='Nombre', unique=True)
    description = models.CharField(max_length=150, verbose_name='Descripcion', null=True)

    def __str__(self):
        # return 'Nombre: {}'.format(self.name)
        return self.name
        
    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ['id']

    def toJSON(self):
        item = {
            'id': self.id,
            'nombre': self.name,
            'descripcion': self.description
        }
        return item



class Product(models.Model):
    name = models.CharField(max_length=150, verbose_name='Nombre', unique=True)
    cate = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product/%Y/%m/%d', null=True, blank=True)
    pvp = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)

    def __str__(self):
        return self.name

    def get_image(self):
        if self.image:
            return f'{MEDIA_URL}{self.image}'
        return f'{STATIC_URL}img/favicon.png'

    def toJSON(self):
        item = {
            'id': self.id,
            'nombre': self.name,
        }
        return item

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        ordering = ['id']


class Client(models.Model):
    names = models.CharField(max_length=150, verbose_name='Nombres')
    surnames = models.CharField(max_length=150, verbose_name='Apellidos')
    dni = models.CharField(max_length=10, unique=True, verbose_name='Dni')
    birthday = models.DateField(default=datetime.now, verbose_name='Fecha de nacimiento')
    address = models.CharField(max_length=150, null=True, blank=True, verbose_name='Dirección')
    sexo = models.CharField(max_length=10, choices=gender_choices, default='male', verbose_name='Sexo')

    def __str__(self):
        return self.names

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        ordering = ['id']


class Sale(models.Model):
    cli = models.ForeignKey(Client, on_delete=models.CASCADE)
    date_joined = models.DateField(default=datetime.now)
    subtotal = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    iva = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    total = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)

    def __str__(self):
        return self.cli.names

    class Meta:
        verbose_name = 'Venta'
        verbose_name_plural = 'Ventas'
        ordering = ['id']


class DetSale(models.Model):
    sale = models.ForeignKey(Sale, on_delete=models.CASCADE)
    prod = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    cant = models.IntegerField(default=0)
    subtotal = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)

    def __str__(self):
        return self.prod.name

    class Meta:
        verbose_name = 'Detalle de Venta'
        verbose_name_plural = 'Detalle de Ventas'
        ordering = ['id']
