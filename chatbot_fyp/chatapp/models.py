from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length= 100)
    email = models.EmailField(blank=False, null=False)
    subject = models.CharField(max_length=50)
    message = models.TextField(blank=False, null=True)