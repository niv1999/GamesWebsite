from django.shortcuts import render
from api.models import ProductSerializer
from products.models import ProductModel
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

# Get JSON of all products
@api_view(["GET"]) # Expose following function only on GET request.
def get_products(request):

    try:
        # Get all products from database:
        products = ProductModel.objects.all()

        # Create a serializer for converting products into json:
        serializer = ProductSerializer(products, many = True) # many = True --> convert into list

        # Response back the serialized json:
        return Response(serializer.data) # Status code = 200 as default
    
    except Exception as err:
        json = { "error": str(err) }
        return Response(json, status = status.HTTP_500_INTERNAL_SERVER_ERROR)


# Get one product:
@api_view(["GET"])
def get_one_products(request, id):

    try:
        product = ProductModel.objects.get(pk=id)
        serializer = ProductSerializer(product)
        return Response(serializer.data) # Status code = 200 as default
    
    except ProductModel.DoesNotExist:
        json = { "error": f"id {id} not found." }
        return Response(json, status= status.HTTP_404_NOT_FOUND)
    
    except Exception as err:
        json = { "error": str(err) }
        return Response(json, status = status.HTTP_500_INTERNAL_SERVER_ERROR)

# Add new product:
@api_view(["POST"]) # Expose following function only on POST request.
def add_product(request):

    try:
        # Get the given product json for adding:
        product = request.data

        # Create serializer for saving that product:
        serializer = ProductSerializer(data = product)

        # Validate:
        if not serializer.is_valid():
            json = { "error": serializer.errors}
            return Response(json, status= status.HTTP_400_BAD_REQUEST) # Validation error
        
        # Save to database:
        serializer.save()

        # Take the added product containing product id:
        added_product = serializer.data

        # Return the added product:
        return Response(added_product, status = status.HTTP_201_CREATED)
    
    except Exception as err:
        json = { "error": str(err) }
        return Response(json, status = status.HTTP_500_INTERNAL_SERVER_ERROR)

# Add new product:
@api_view(["PUT"]) # Expose following function only on POST request.
def edit_product(request, id):

    try:

        # If product not found:
        exist = ProductModel.objects.filter(id = id).exists()
        if not exist:
            json = { "error": f"id {id} not found." }
            return Response(json, status= status.HTTP_404_NOT_FOUND)
        
        # Get the given product json for edit:
        product = request.data

        # Create serializer for saving that product:
        serializer = ProductSerializer(data = product, instance= ProductModel(pk = id))

        # Validate:
        if not serializer.is_valid():
            json = { "error": serializer.errors}
            return Response(json, status= status.HTTP_400_BAD_REQUEST) # Validation error
        
        # Save to database:
        serializer.save()

        # Take the updated product containing product id:
        updated_product = serializer.data

        # Return the updated product:
        return Response(updated_product) # Status code = 200 as default
    
    except ProductModel.DoesNotExist:
        json = { "error": f"id {id} not found." }
        return Response(json, status= status.HTTP_404_NOT_FOUND)
    
    except Exception as err:
        json = { "error": str(err) }
        return Response(json, status = status.HTTP_500_INTERNAL_SERVER_ERROR)

# Delete existing product:
@api_view(["DELETE"])
def delete_product(request, id):

    try:

        # If product not found:
        exist = ProductModel.objects.filter(id = id).exists()
        if not exist:
            json = { "error": f"id {id} not found." }
            return Response(json, status= status.HTTP_404_NOT_FOUND)
        
        # Create dummy product for delete:
        dummy_product = ProductModel(pk = id)

        # Delete this product from the database:
        dummy_product.delete()

        # Response back nothing:
        return Response(status= status.HTTP_204_NO_CONTENT)
    
    except ProductModel.DoesNotExist:
        json = { "error": f"id {id} not found." }
        return Response(json, status= status.HTTP_404_NOT_FOUND)
    
    except Exception as err:
        json = { "error": str(err) }
        return Response(json, status = status.HTTP_500_INTERNAL_SERVER_ERROR)