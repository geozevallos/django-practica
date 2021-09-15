from django.db import models
from datetime import datetime

from django.db.models.deletion import CASCADE

# Create your models here.

class Type(models.Model):
    name = models.CharField(max_length=150, verbose_name="Nombre")

    # Metodo str, to string
    def __str__(self):
        return self.name

    # LA clse meta para propiedades
    db_table = 'tipo'
    verbose_name = 'Tipo'
    verbose_name_plural = 'Tipos'
    ordering = ['id']


class Category(models.Model):
    name = models.CharField(max_length=150, verbose_name="Nombre")

    # Metodo str, to string
    def __str__(self):
        return self.name

    # LA clse meta para propiedades
    db_table = 'categoria'
    verbose_name = 'Categoria'
    verbose_name_plural = 'Categorias'
    ordering = ['id']



class Employee(models.Model):
    # Para relacionar la tabla
    category = models.ManyToManyField(Category)
    type = models.ForeignKey(Type, on_delete=models.CASCADE) #models.protect para proteger
    names = models.CharField(max_length=150, verbose_name="Nombres")
    dni = models.CharField(max_length=8, verbose_name="DNI"),
    date_joined = models.DateField(default=datetime.now, verbose_name="Fecha de registro")
    date_creation = models.DateTimeField(auto_now=True)
    date_update = models.DateTimeField(auto_now_add=True)
    age = models.PositiveIntegerField(default=0)
    salary = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    gender = models.CharField(max_length=20, null=True, blank=True)
    status = models.BooleanField(default=True)
    avatar = models.ImageField(upload_to='avatar/%Y/%m/%d', null=True, blank=True)
    cvitae = models.FileField(upload_to='cvitae/%Y/%m/%d', null=True, blank=True)

    # Metodo str, to string
    def __str__(self):
        return self.names

    # LA clse meta para propiedades
    db_table = 'empleado'
    verbose_name = 'Empleado'
    verbose_name_plural = 'Empleados'
    ordering = ['id']