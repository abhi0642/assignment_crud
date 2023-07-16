from django.db import models

class User(models.Model):
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    role = models.CharField(max_length=255, choices=[('admin', 'Admin'), ('manager', 'Manager'), ('staff', 'Staff')])

class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    inventory_count = models.IntegerField()