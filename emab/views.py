from django.shortcuts import render
from rest_framework import generics
from .models import Category, Toner, Product
from .serializers import CategorySerializer, TonerSerializer, ProductSerializer
# Create your views here.
class CategoryList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ListToner(generics.ListCreateAPIView):
    queryset = Toner.objects.all()
    serializer_class = TonerSerializer

class DetailToner(generics.RetrieveUpdateDestroyAPIView):
    queryset = Toner.objects.all()
    serializer_class = TonerSerializer

class ListProduct(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class DetailProduct(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer