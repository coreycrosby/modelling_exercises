from django.db import models


class Customer(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    mailing_address = models.CharField(max_length=255)


class Order(models.Model):
    order_number = models.CharField(max_length=255)
    date = models.DateTimeField()
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name="orders")


class Author(models.Model):
    name = models.CharField(max_length=255)


class Book(models.Model):
    title = models.CharField(max_length=255)
    isbn = models.CharField(max_length=255)
    author_id = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="books")
    