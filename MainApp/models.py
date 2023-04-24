from django.db import models

# Create your models here.

# CHAT

class ContactForm(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


# class ContactoForm(models.Model):
#     nombre = models.CharField(max_length=50)
#     email = models.EmailField()
#     mensaje = models.TextField()

#     def __str__(self):
#         return self.nombre