from django.urls import path
from .views import CategoryList, CategoryDetail, ListToner, DetailToner, ListProduct, DetailProduct
urlpatterns = [
    path('categories', CategoryList.as_view(), name='categories'),
    path('categories/<int:pk>/', CategoryDetail.as_view(), name='singlecategory'),
    path('toners', ListToner.as_view(), name='toners'),
    path('toners/<int:pk>/', DetailToner.as_view(), name='singletoner'),
    path('products', ListProduct.as_view(), name='products'),
    path('products/<int:pk>/', DetailProduct.as_view(), name='singleproduct')
]