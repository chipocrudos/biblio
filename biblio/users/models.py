from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager,
                                        PermissionsMixin)
from django.db import models


class UserProfileManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, first_name, last_name, password=None,
                     **extra_fields):
        if not email:
            raise ValueError('Email es requerido')

        if not first_name:
            raise ValueError('Nobre o nombres es requerido')

        if not last_name:
            raise ValueError('Apellido o apellidos es requerido')

        email = self.normalize_email(email)

        user = self.model(email=email, first_name=first_name,
                          last_name=last_name, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, first_name, last_name, password=None,
                    **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_superuser', False)

        return self._create_user(email, first_name, last_name, password,
                                 **extra_fields)

    def create_superuser(self, email, first_name, last_name, password,
                         **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, first_name, last_name, password,
                                 **extra_fields)


class UserProfile(AbstractBaseUser, PermissionsMixin):
    '''Model base sistema'''

    email = models.EmailField(max_length=255, unique=True)
    first_name = models.CharField(max_length=80)
    last_name = models.CharField(max_length=200)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    phone = models.CharField(max_length=20, blank=True, null=True)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    class Meta:
        managed = True
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        ordering = ['last_name', 'first_name', 'email']

    def __str__(self) -> str:
        return f'{self.email}'

    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'.strip()
