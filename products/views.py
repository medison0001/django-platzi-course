from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from products.serializers import ProductSerializer
from .forms import ProductFrom
from .models import Product
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
class ProductFormView(generic.FormView):
    template_name = "products/add_producto.html"
    form_class = ProductFrom
    success_url = reverse_lazy("list_product")

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

class ProductListView(generic.ListView):
    model = Product
    template_name = 'products/list_product.html'
    context_object_name = 'products'

class ProductListAPI(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)