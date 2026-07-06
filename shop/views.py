from django.contrib import messages
from django.shortcuts import redirect
from django.shortcuts import render, get_object_or_404
from .models import Product, Category , Contact 
from django.db.models import Q
from django.core.paginator import Paginator


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

    products = Product.objects.all()

    category_slug = request.GET.get("category")

    search_query = request.GET.get("q")


    if category_slug:
        products = products.filter(
            category__slug=category_slug
        )

    if search_query:
        products = products = products.filter(
            
        Q(name__icontains=search_query) |
        Q(description__icontains=search_query) |
        Q(category__name__icontains=search_query)
        #__icontains(lookup in Django) in name,not = "" 
    )
        

    paginator = Paginator(products, 1)

    page_number = request.GET.get("page")

    products = paginator.get_page(page_number)


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




def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        message_text = request.POST.get("message")

        Contact.objects.create(
            name=name,
            email=email,
            subject=subject,
            message=message_text,
        )
        messages.success(
            request,
            "پیام شما با موفقیت ارسال شد."
        )

        return redirect("contact")

    return render(request, "contact.html")


    