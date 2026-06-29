from django.urls import path

from .views import (
    store,
    product_detail
)

urlpatterns = [
    path(
        "",
        store,
        name="store"
    ),

    path(
        "product/<slug:slug>/",
        product_detail,
        name="product_detail"
    ),
]