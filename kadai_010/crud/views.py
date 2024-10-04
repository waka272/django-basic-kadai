from django.views.generic import DetailView
from .models import Product

class ProductDetailVeiw(DetailView):
    model=Product
