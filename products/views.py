from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from .forms import ProductFrom
from .models import Product

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