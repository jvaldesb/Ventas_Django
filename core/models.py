from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    email = models.EmailField('email address', unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'

class Client(models.Model):
    DOCUMENT_TYPE_CHOICES = [
        ('TI', 'Tarjeta de Identidad'),
        ('CC', 'Cedula de Ciudadania'),
        ('CE', 'Cedula de Extranjeria'),
        ('PA', 'Pasaporte')
    ]
    document_type = models.CharField('Tipo de Documento', max_length=2, choices=DOCUMENT_TYPE_CHOICES)
    document = models.CharField('Número de Documento', max_length=12, unique=True)
    first_name = models.CharField('Nombre(s)', max_length=30)
    last_name = models.CharField('Apellido(s)', max_length=30)
    email = models.EmailField('Correo electronico')

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'

    def __str__(self):
        return self.document + " " + self.first_name + " " + self.last_name


class Bill(models.Model):
    client = models.ForeignKey(Client, 'Cliente')
    company_name = models.CharField('Empresa', max_length=80)
    nit = models.CharField('Nit', max_length=9, help_text='Ingrese en nit de la empresa sin código de verificación')
    code = models.CharField('Código de verificación', max_length=1)

    class Meta:
        verbose_name = 'Factura'
        verbose_name_plural = 'Facturas'

    def __str__(self):
        return "F# " + str(self.id) + " " + self.company_name + " " + str(self.client_id)


class Attribute(models.Model):
    attribute = models.CharField('Atributo', max_length=100)
    value = models.CharField('Valor', max_length=100)

    class Meta:
        verbose_name = 'Atributo'
        verbose_name_plural = 'Atributos'

    def __str__(self):
        return self.attribute


class Product(models.Model):
    name = models.CharField('Nombre', max_length=120)
    description = models.TextField('Descripción', max_length=500)
    Attribute = models.ManyToManyField(Attribute, 'Atributos')

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'

    def __str__(self):
        return str(self.id) + " " + self.name


class BillProduct(models.Model):
    bill_id = models.ForeignKey(Bill, 'Factura')
    product_id = models.ForeignKey(Product, 'Producto')
