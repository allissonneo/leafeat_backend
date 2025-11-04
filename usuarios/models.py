from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.utils import timezone

class UsuarioManager(BaseUserManager):
    def create_user(self, email, senha=None, **extra_fields):
        if not email:
            raise ValueError("O usuário deve ter um email")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        if senha:
            user.set_password(senha)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, senha=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, senha, **extra_fields)

class Usuario(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    nome_completo = models.CharField(max_length=255, blank=True)
    senha_hash = models.CharField(max_length=255, blank=True)
    provedor_oauth = models.CharField(max_length=32, blank=True, null=True)
    oauth_id = models.CharField(max_length=255, blank=True, null=True)
    avatar_url = models.TextField(blank=True, null=True)
    ativo = models.BooleanField(default=True)
    funcionario = models.BooleanField(default=False)
    revisor_confiavel = models.BooleanField(default=False)
    criado_em = models.DateTimeField(default=timezone.now, editable=False)
    atualizado_em = models.DateTimeField(default=timezone.now)

    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UsuarioManager()

    def __str__(self):
        return self.email
