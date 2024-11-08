from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from rest_framework.views import APIView
from rest_framework.response import Response

from products.forms import ProductForm
from products.models import Product
from products.serializer import ProductSerializer

# Create your views here.
class ProductFormView(generic.FormView):
    template_name = 'add_product.html'
    form_class = ProductForm
    success_url = reverse_lazy('add_product')
    
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    
    
class ProductListView(generic.ListView):
    model = Product
    template_name = 'list_products.html'
    context_object_name = 'products'
    
    
class ProductListApi(APIView):
    permission_classes = []
    authentication_classes = []
    
    def get(self, request, *args, **kwargs):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        
        return Response(serializer.data)