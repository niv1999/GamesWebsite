from django.db import models
from rest_framework.serializers import ModelSerializer
from products.models import ProductModel

# Tell REST Framework how to convert product into json:
class ProductSerializer(ModelSerializer):

    class Meta:
        model = ProductModel
        fields = "__all__" # All fields
        