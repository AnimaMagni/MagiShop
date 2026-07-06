from django.urls import path

from .views import (
    store,
    product_detail,
    home,
    contact
    
)

urlpatterns = [

    path(
        "",
        home,
        name="home"
    ),

    path(
        "store/",
        store,
        name="store"
    ),

    path(
        "product/<slug:slug>/",
        product_detail,
        name="product_detail"
    ),

    path(
        "contact/",
        contact,
        name="contact"
    ),
]