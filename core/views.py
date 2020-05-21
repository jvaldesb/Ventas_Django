from django.shortcuts import render
from rest_framework import viewsets, generics, response, views, permissions, status, renderers
from django.http import Http404
from django.core.serializers import serialize
from . import models, serializer as seri
from django.db import connection
import csv


class ClientViewset(viewsets.ModelViewSet):
    queryset = models.Client.objects.all()
    serializer_class = seri.ClientSerializer
    permission_classes = [permissions.IsAuthenticated]


class BillViewset(viewsets.ModelViewSet):
    queryset = models.Bill.objects.all()
    serializer_class = seri.BillSerializer
    permission_classes = [permissions.IsAuthenticated]


class AttributeViewset(viewsets.ModelViewSet):
    queryset = models.Attribute.objects.all()
    serializer_class = seri.AttributeSerializer
    permission_classes = [permissions.IsAuthenticated]


class ProductViewset(viewsets.ModelViewSet):
    queryset = models.Product.objects.all()
    serializer_class = seri.ProductSerializer
    permission_classes = [permissions.IsAuthenticated]


class BillProductViewset(viewsets.ModelViewSet):
    queryset = models.BillProduct.objects.all()
    serializer_class = seri.BillProductSerializer
    permission_classes = [permissions.IsAuthenticated]


class ClientCsv(views.APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        try:
            document = request.query_params['document']
            client = models.Client.objects.raw("SELECT * FROM core_client WHERE document='" + document + "'")[0]
            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM core_bill WHERE client_id=%s", str(client.id))
                row = cursor.fetchone()
                print(row)
            print(client)
            return response.Response({'status': 'procesado'}, 200)
        except Exception as e:
            return response.Response(status=status.HTTP_400_BAD_REQUEST)
