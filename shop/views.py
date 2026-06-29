from django.shortcuts import render, get_object_or_404

from .models import Product


def store(request):
    products = Product.objects.filter(is_featured=True)
    return render(request, "store/store.html", {"products": products})


#def product_detail(request, id):
def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    return render(request, "store/product_detail.html", {"product": product})
