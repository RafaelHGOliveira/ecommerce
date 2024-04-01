from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager


class MyUserManager(BaseUserManager):
    def create_user(self, email, date_of_birth, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError("Users must have an email address")

        user = self.model(
            email=self.normalize_email(email),
            date_of_birth=date_of_birth,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, date_of_birth, password=None):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            email,
            password=password,
            date_of_birth=date_of_birth,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user
    

class User(AbstractUser):
    cpf = models.CharField('CPF', max_length=11, null=True, blank=True)
    birth_date = models.DateField('Data de Nascimento', null=True, blank=True)
    phone_number = models.CharField('Telefone', max_length=11, null=True, blank=True)
    genre = models.CharField('Genero', max_length=255, null=True, blank=True)
    
    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
        
    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'

class Address(models.Model):
    street = models.CharField('Rua', max_length=255, null=True)
    number = models.CharField('Numero', max_length=10, null=True)
    district = models.CharField('Estado', max_length=255, null=True)
    city = models.CharField('Cidade', max_length=255, null=True)
    state = models.CharField('Estado', max_length=255, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name = 'Usuario')
    
    class Meta:
        verbose_name = 'Endereço'
        verbose_name_plural = 'Endereços'
        
    def __str__(self) -> str:
        return f'{self.address}, {self.number}, {self.district}, {self.city}, {self.state},'
