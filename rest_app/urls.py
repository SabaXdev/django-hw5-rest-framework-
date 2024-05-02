from django.urls import path
from rest_app.views import ProductListCreateView, ProductRetrieveUpdateDeleteView

app_name = 'rest_app'

urlpatterns = [
    path('products/<int:product_id>/', ProductRetrieveUpdateDeleteView.as_view(), name='get_product'),
    path('products/', ProductListCreateView.as_view(), name='get_products')
]
