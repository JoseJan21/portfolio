from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

User = get_user_model()

def get_current_user(request):
    return User.objects.get(username=request.user.username) if request.user.is_authenticated else None

class Tareas(models.Model):
    subject = models.CharField(max_length=100, verbose_name='Nombre de la rutina')
    description = models.CharField(max_length=300, verbose_name='Descripción')
    is_done = models.BooleanField(default=False, verbose_name='¿Completada?')
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None, editable=False, verbose_name='Usuario')
    
    def save(self, *args, **kwargs):
        request = kwargs.get('request')
        if request:
            self.user = get_current_user(request)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.subject