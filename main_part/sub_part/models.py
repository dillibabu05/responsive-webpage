from django.db import models

# Create your models here.
class register_table(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    password=models.CharField(max_length=30)
    email=models.EmailField(max_length=30)
    phone=models.TextField(max_length=10)
    profile_picture=models.ImageField(upload_to='documents')


#  contact 
class contact_table(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=30)
    subject=models.CharField(max_length=20)
    message=models.CharField(max_length=100)

