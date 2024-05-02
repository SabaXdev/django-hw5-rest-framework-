from rest_framework.authentication import BasicAuthentication
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_app.models import Product
from rest_app.serializers import ProductSerializer, ProductListSerializer, ProductUpdateSerializer
from rest_framework import status


class ProductListCreateView(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer
    pagination_class = PageNumberPagination

    def get_permissions(self):
        if self.request.method == 'POST':
            return [IsAuthenticated()]
        return super().get_permissions()

    def get_authenticators(self):
        if self.request.method == 'POST':
            return [BasicAuthentication()]
        return super().get_authenticators()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ProductListSerializer
        return ProductSerializer


class ProductRetrieveUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_url_kwarg = 'product_id'

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ProductSerializer
        return ProductUpdateSerializer

    def delete(self, request, *args, **kwargs):
        product_id = kwargs.get('product_id')
        product = self.get_object()
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
