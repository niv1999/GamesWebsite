from django.urls import path
from . import views

urlpatterns = [
    # GET http://localhost:8000/api/products
    path("products", views.get_products),

    # GET http://localhost:8000/api/products/1
    path("products/<int:id>", views.get_one_products),

    # GET http://localhost:8000/api/products/new
    path("products/new", views.add_product),

    # GET http://localhost:8000/api/products/edit/1
    path("products/edit/<int:id>", views.edit_product),

    # GET http://localhost:8000/api/products/delete/1
    path("products/delete/<int:id>", views.delete_product)

]
