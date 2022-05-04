from pyexpat import model
from django.shortcuts import render
from django.views.generic import ListView
from .models import Product

# Create your views here.
class ProductsList(ListView):
    template_name = 'products.html'
    model = Product
    context_object_name = 'products'
    paginate_by = 6

    def get_queryset(self, *args, **kwargs):
        products = Product.objects.all()
        return products

class HomePage(ListView):
    template_name = 'home.html'
    model = Product
