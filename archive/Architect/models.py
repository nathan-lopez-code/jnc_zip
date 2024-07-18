from django.db import models
from .utils import connect_image_deletion_signals
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
# Create your models here.

class CustomUserManager(BaseUserManager):
    def create_user(self, name, password=None, **extra_fields):
        if not name:
            raise ValueError('The Name field must be set')
        user = self.model(name=name, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, name, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(name, password, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(max_length=50, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'name'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.name
class Building(models.Model):
    address = models.CharField(max_length=255)
    server_user = models.CharField(max_length=255) 
    construction_year = models.IntegerField(blank=True, null=True)
    etat_immeuble = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    observation = models.TextField(blank=True,null=True)

class Archive(models.Model):
    image = models.ImageField(upload_to='archives/')
    description = models.TextField()
    state = models.CharField(max_length=255,blank=True,null=True)
    plan_2d = models.ImageField(upload_to='plans/2d/')
    plan_3d = models.ImageField(upload_to='plans/3d/')

class ChefProject(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='chefs/')
    qualification = models.CharField(max_length=255)
    class Meta:
        verbose_name = 'Contacts'

class Widgets(models.Model):
    image = models.ImageField(upload_to='home/')
    caption = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.caption or "Home Image"
    
connect_image_deletion_signals(Archive)
connect_image_deletion_signals(ChefProject)
connect_image_deletion_signals(Widgets)
