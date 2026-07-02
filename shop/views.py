from django.shortcuts import render, get_object_or_404
from .models import Product, Category


def home(request):
    categories = Category.objects.all()
    featured_products = Product.objects.filter(
        is_featured=True
    ).order_by("-created_at")[:4]

    new_products = Product.objects.order_by("-created_at")[:4]

    return render(
        request,
        "home.html",
        {
            "featured_products": featured_products,
            "new_products": new_products,
            "categories": categories,
        }
    )

def store(request):

    categories = Category.objects.all()

    category_slug = request.GET.get("category")

    if category_slug:
        products = products.filter(
            category__slug=category_slug
        )

    products = Product.objects.filter(
        is_featured=True
    )


    return render(
        request,
        "store/store.html",
        {
            "products": products,
            "categories": categories,
        }
    )


#def product_detail(request, id):
def product_detail(request, slug):

    product = get_object_or_404(
        Product,
        slug=slug
    )

    return render(
        request,
        "store/product_detail.html",
        {
            "product": product
        }
    )