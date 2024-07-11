from django.db.models import Model, CharField, DecimalField, IntegerField, ForeignKey, RESTRICT, DateField
from django.forms import DateInput, ModelForm, NumberInput, Select, TextInput
from datetime import datetime
from django.core.validators import MinLengthValidator, MaxLengthValidator, MinValueValidator, MaxValueValidator

# Category model:
class CategoryModel(Model):

    # First column - id - will be created automatically.

    # Second column:
    name = CharField(max_length = 50)

    #__str__ magic method:
    def __str__(self):
        return self.name

    # Metadata:
    class Meta:
        db_table = "categories"


# ------------------------------------------------------------------------------------


# Product model:
class ProductModel(Model):

    # First column - id - will be created automatically.

    # Second column:
    name = CharField(max_length = 50, validators=[MinLengthValidator(2), MaxLengthValidator(100)])

    # Third column:
    price = DecimalField(max_digits = 6, decimal_places = 2, validators=[MinValueValidator(0, "Price can't be negative."), MaxValueValidator(1000)])

    # Fourth column:
    stock = IntegerField(validators=[MinValueValidator(0), MaxValueValidator(1000)])

    # Fifth column (relation):
    category = ForeignKey(CategoryModel, on_delete = RESTRICT)

    # Sixth column:
    release_date = DateField(default = datetime.now)

    # Metadata:
    class Meta:
        db_table = "products"



# ------------------------------------------------------------------------------------

class ProductForm(ModelForm):
    
    class Meta:
        model = ProductModel
        fields = ["name", "price", "stock", "category", "release_date"]
        # exclude = ["id"]

        widgets = {
            "name": TextInput(attrs= { "class": "form-control", "minlength":2, "maxlength":100}), # attrs = HTML attributes
            "price": NumberInput(attrs= { "class": "form-control", "min":0, "max":1000}),
            "stock": NumberInput(attrs= { "class": "form-control", "min":0, "max":1000}),
            "category": Select(attrs= { "class": "form-control"}),
            "release_date": DateInput(attrs= { "class": "form-control", "type":"date"})
        }