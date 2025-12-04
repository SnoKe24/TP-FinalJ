from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.

class Usuario(AbstractUser):
    username = None
    email = models.EmailField(unique=True)
    nombre = models.CharField(max_length=50)

    ROLES = (
        ('superadmin', 'Super Administrador'),
        ('cliente', 'Cliente'),
    )

    rol = models.CharField(max_length=20, choices=ROLES, default='cliente')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


