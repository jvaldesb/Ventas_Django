# **API Ventas_Django 🏁**
___________________________________
>API desarrollada por Julián Valdés

>>Adjunto coleccion PostMAn con los endpoint.

## INFORMACIÓN

Esta es una API desarrollada para la prueba de Quick Smart: cuenta con todos los métodos como **GET**, **HEAD**, **POST**, **PUT**, **DELETE** entre otras. Por temas de tiempo, el desarrollo se usaron metodos abstractos.

## DESPLIGUE

### BIBLIOTECAS Y LENGUAJES
- Python 3.8
- Django 2.2.9
- DRF 3.11.0
- djoser 2.0.3
- DRF-SimpleJWT 4.4.0

```
pip install Django==2.2.9
pip install djangorestframewor==3.11.0
pip install djangorestframewor-simplejwt==4.4.0
pip install djoser==2.0.3
```

## PUNTOS FINALES
> Todos los puntos finales requieren Token Bearer en la cabecera

* ### Crear usuario
Use este punto final para registrar un nuevo usuario.

**URL**: ``/api/v1/auth/users/``
**METODOS**: ``POST, HEAD, OPTIONS`` 
```
{
    "username": "",
    "password": "",
    "email": "",
}
```

* ### Iniciar sesión (crear JWT)
Use este punto final para iniciar sesión

**URL**: ``/api/v1/auth/jwt/create/`` 
**METODOS**: ``POST, HEAD, OPTIONS`` 
```
{
    "username": "",
    "password": "",
}
```

* ### Actualizar sesión (refrescar JWT)
Use este punto final para refrescar sesión

**URL**: ``/api/v1/auth/jwt/refresh/`` 
**METODOS**: ``POST, HEAD, OPTIONS`` 
```
{
    "refresh": "",
}
```

* ### Cliente
Use este grupo de metodos para crear, eliminar, actualizar, y renderizar un cliente

**URL**: ``/api/v1/client`` 
**METODOS**: ``POST, GET, PUT, DELETE, HEAD, OPTIONS`` 
```
{
    "document_type": "choices": [
                    {
                        "value": "TI",
                        "display_name": "Tarjeta de Identidad"
                    },
                    {
                        "value": "CC",
                        "display_name": "Cedula de Ciudadania"
                    },
                    {
                        "value": "CE",
                        "display_name": "Cedula de Extranjeria"
                    },
                    {
                        "value": "PA",
                        "display_name": "Pasaporte"
                    }
                ]
    "document": "",
    "first_name": "",
    "last_name": "",
    "email": ""
}
```

* ### Factura
Use este grupo de metodos para crear, eliminar, actualizar, y renderizar una Factura

**URL**: ``/api/v1/bill`` 
**METODOS**: ``POST, GET, PUT, DELETE, HEAD, OPTIONS`` 
```
{
    "company_name": "",
    "nit": "",
    "code": "",
    "client": 
}
```
* ### Produtos
Use este grupo de metodos para crear, eliminar, actualizar, y renderizar un producto

**URL**: ``/api/v1/product`` 
**METODOS**: ``POST, GET, PUT, DELETE, HEAD, OPTIONS`` 
```
{
    "id": 1,
    "name": "Reloj Dorado",
    "description": "Reloj dorado metal",
    "Attribute": [
        1
    ]
}
```

* ### Atributos
Use este grupo de metodos para crear, eliminar, actualizar, y renderizar un atributo de producto

**URL**: ``/api/v1/product`` 
**METODOS**: ``POST, GET, PUT, DELETE, HEAD, OPTIONS`` 
```
{
    "attribute": "",
    "value": ""
}
```

* ### Agregar producto a una factura
Use este grupo de metodos para crear, eliminar, actualizar, y renderizar productos en una factura

**URL**: ``/api/v1/product`` 
**METODOS**: ``POST, GET, PUT, DELETE, HEAD, OPTIONS`` 
```
{
    "bill_id": ,
    "product_id": 
}
```




