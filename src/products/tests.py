from django.test import SimpleTestCase, TestCase, Client
from django.urls import reverse, resolve
from products.models import CategoryModel, ProductModel
from .views import sales, list, details, categories, insert, edit, delete, info
from http import HTTPStatus
from django.contrib.auth.models import User

class TestUrls(SimpleTestCase):

    def test_urls(self):

        url = reverse("sales") # 'sales' = the name
        view_function = resolve(url).func 
        self.assertEqual(view_function, sales)

        url = reverse("products")
        view_function = resolve(url).func 
        self.assertEqual(view_function, list)

        url = reverse("details", args = [1])
        view_function = resolve(url).func 
        self.assertEqual(view_function, details)

        url = reverse("categories")
        view_function = resolve(url).func 
        self.assertEqual(view_function, categories)

        url = reverse("insert")
        view_function = resolve(url).func 
        self.assertEqual(view_function, insert)

        url = reverse("edit", args = [1])
        view_function = resolve(url).func 
        self.assertEqual(view_function, edit)

        url = reverse("delete", args = [1])
        view_function = resolve(url).func 
        self.assertEqual(view_function, delete)

        url = reverse("info")
        view_function = resolve(url).func 
        self.assertEqual(view_function, info)

class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        beverages = CategoryModel.objects.create(name = "Beverages")
        ProductModel.objects.create(name = "Water", price = 5, stock = 50, category = beverages, release_date = "2024-01-02")
        ProductModel.objects.create(name = "Sprite", price = 8, stock = 60, category = beverages, release_date = "2024-01-02")
        ProductModel.objects.create(name = "Ice Tea", price = 10, stock = 80, category = beverages, release_date = "2024-01-02")
        test_username = "tester@gmail.com"
        test_password = "Testing1234"
        User.objects.create_superuser(username = test_username, password = test_password)
        self.client.login(username = test_username, password = test_password)


    def test_sales(self):
        url = reverse("sales")
        response = self.client.get(url)
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(response, "sales.html")


    def test_list(self):
        url = reverse("products")
        response = self.client.get(url)
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(response, "products.html")
        self.assertContains(response, "Water")
        self.assertContains(response, "Sprite")
        self.assertContains(response, "Ice Tea")


    def test_details(self):
        url = reverse("details", args = [1])
        response = self.client.get(url)
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(response, "details.html")
        self.assertContains(response, "Water")

    
    def test_insert_get(self):
        url = reverse("insert")
        response = self.client.get(url)
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(response, "insert.html")
        self.assertContains(response, "<form")
        self.assertContains(response, "</form")

    
    def test_insert_post(self):
        url = reverse("insert")
        form_data = {"name": "Orange Juice", "price": 10, "stock": 50, "category": 1, "release_date": "2024-02-23"}
        response = self.client.post(url, data = form_data, follow = True) # follow = True --> tell the client to follow all redirection until final result.
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(response, "products.html")
        exist_in_db = ProductModel.objects.filter(name = "Orange Juice").exists()
        self.assertTrue(exist_in_db)
        self.assertContains(response, "Orange Juice")


    def test_edit_get(self):
        url = reverse("edit", args =  [1])
        response = self.client.get(url)
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(response, "edit.html")
        self.assertContains(response, "<form")
        self.assertContains(response, "</form")

    
    def test_edit_post(self):
        url = reverse("edit", args = [1])
        form_data = {"id": 1, "name": "Orange Juice", "price": 10, "stock": 50, "category": 1, "release_date": "2024-02-23"}
        response = self.client.post(url, data = form_data, follow = True)
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(response, "products.html")
        exist_in_db = ProductModel.objects.filter(name = "Orange Juice").exists()
        self.assertTrue(exist_in_db)
        self.assertContains(response, "Orange Juice")


    def test_delete(self):
        url = reverse("delete", args = [1])
        response = self.client.get(url, follow = True)
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(response, "products.html")
        exists_in_db = ProductModel.objects.filter(id = 1).exists()
        self.assertFalse(exists_in_db)
