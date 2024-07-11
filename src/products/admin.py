from django.contrib.admin import ModelAdmin, site
from products.models import CategoryModel, ProductModel

# How to admin a category:
class CategoryAdmin(ModelAdmin):
    list_display = ("id", "name")

# How to admin a product:
class ProductAdmin(ModelAdmin):
    list_display = ("id", "name", "price", "stock", "category", "release_date")
    list_display_links = ("name", )

# Connect between admin and models:
site.register(CategoryModel, CategoryAdmin)
site.register(ProductModel, ProductAdmin)

