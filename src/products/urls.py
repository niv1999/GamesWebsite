from django.urls import path
from . import views

urlpatterns = [
    path("sales", views.sales, name="sales"),

    path("", views.list, name="products"),

    path("details/<int:id>", views.details, name="details"),

    path("categories", views.categories, name="categories"),

    path("new", views.insert, name="insert"),

    path("edit/<int:id>", views.edit, name="edit"),

    path("delete/<int:id>", views.delete, name="delete"),

    path("info", views.info, name="info")
]
