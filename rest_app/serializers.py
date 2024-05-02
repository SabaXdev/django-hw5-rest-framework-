from rest_framework.serializers import ModelSerializer
from rest_app.models import Product


# For POST and DELETE methods
class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


# For GET method
class ProductListSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = ['name', 'price']


# For PUT method
class ProductUpdateSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = ['stock']