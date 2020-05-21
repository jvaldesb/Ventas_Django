from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'client', views.ClientViewset, basename='clien')
router.register(r'bill', views.BillViewset, basename='bill')
router.register(r'attribute', views.AttributeViewset, basename='attribute')
router.register(r'product', views.ProductViewset, basename='product')
router.register(r'billproduct', views.BillProductViewset, basename='billproduct')


urlpatterns = [
    path('', include(router.urls)),
    path('client_csv', views.ClientCsv.as_view(), name="client_csv")
]