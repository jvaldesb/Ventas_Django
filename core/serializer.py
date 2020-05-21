from djoser.serializers import UserCreateSerializer
from rest_framework import serializers
from . import models

class UserRegistrationSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        fields = ('username', 'password', 'email')

class ClientSerializer(serializers.ModelSerializer):
    # Clase clientes que hereda del la clase ModelSerializer
    class Meta:
        # Contenedor de metadatos
        model = models.Client
        fields = '__all__'

class BillSerializer(serializers.ModelSerializer):
    # Clase clientes que hereda del la clase ModelSerializer
    class Meta:
        # Contenedor de metadatos
        model = models.Bill
        fields = '__all__'


class AttributeSerializer(serializers.ModelSerializer):
    # Clase clientes que hereda del la clase ModelSerializer
    class Meta:
        # Contenedor de metadatos
        model = models.Attribute
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    # Clase clientes que hereda del la clase ModelSerializer
    class Meta:
        # Contenedor de metadatos
        model = models.Product
        fields = '__all__'

class BillProductSerializer(serializers.ModelSerializer):
    # Clase clientes que hereda del la clase ModelSerializer
    class Meta:
        # Contenedor de metadatos
        model = models.BillProduct
        fields = '__all__'