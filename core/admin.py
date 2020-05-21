from django.contrib import admin
from .models import Client, Bill, Product, Attribute, BillProduct

admin.site.register(Client)
admin.site.register(Bill)
admin.site.register(Product)
admin.site.register(Attribute)
admin.site.register(BillProduct)
