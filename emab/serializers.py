from rest_framework import serializers
from .models import Category, Toner, Product

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        fields = (
            'title'
        )
        model = Category

class TonerSerializer(serializers.ModelSerializer):

    class Meta:
        fields = (
            'id',
            'title',
            'category',
            'color',
            'price',
            'stock',
            'description',
            'imageUrl',
            'status',
        )
        model = Toner

class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        fields = (
            'id',
            'product_tag', 
            'title', 
            'name', 
            'category', 
            'price', 
            'stock', 
            'description', 
            'imageUrl', 
            'status', 
            'date_created'
        )
        model = Product