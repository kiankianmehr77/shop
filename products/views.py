from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Product
from django.views import View


class ProductDetailView(View):
    def get(self, request, slug):
        product = get_object_or_404(Product,slug = slug)
        return render(request,"products/detail.html", {'product':product})