from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from .forms import ProductFrom

# Create your views here.
class ProductFormView(generic.FormView):
    template_name = "products/add_producto.html"
    form_class = ProductFrom
    success_url = reverse_lazy("add_product")

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
