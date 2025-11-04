from django.db import models
from usuarios.models import Usuario
from django.utils import timezone

class Endereco(models.Model):
    rua = models.CharField(max_length=255, blank=True, null=True)
    numero = models.CharField(max_length=50, blank=True, null=True)
    bairro = models.CharField(max_length=255, blank=True, null=True)
    cidade = models.CharField(max_length=120)
    estado = models.CharField(max_length=2)
    cep = models.CharField(max_length=20, blank=True, null=True)
    referencia = models.CharField(max_length=255, blank=True, null=True)
    latitude = models.DecimalField(max_digits=10, decimal_places=7, blank=True, null=True)
    longitude = models.DecimalField(max_digits=10, decimal_places=7, blank=True, null=True)

    def __str__(self):
        return f"{self.rua}, {self.numero} - {self.cidade}/{self.estado}"

class Restaurante(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='restaurantes', blank=True, null=True)
    nome = models.CharField(max_length=255)
    email = models.EmailField(unique=True, blank=True, null=True)
    senha_hash = models.CharField(max_length=255, blank=True, null=True)
    cnpj = models.CharField(max_length=32, unique=True, blank=True, null=True)
    telefone = models.CharField(max_length=40, blank=True, null=True)
    descricao = models.TextField(blank=True, null=True)
    endereco = models.ForeignKey(Endereco, on_delete=models.SET_NULL, null=True)
    tipo_cozinha = models.CharField(max_length=100, blank=True, null=True)
    nivel_saude_medio = models.SmallIntegerField(blank=True, null=True)
    emblema_sustentavel = models.BooleanField(default=False)
    emblema_cardapio_metrificado = models.BooleanField(default=False)
    ativo = models.BooleanField(default=True)
    criado_em = models.DateTimeField(default=timezone.now, editable=False)
    atualizado_em = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.nome

class Prato(models.Model):
    restaurante = models.ForeignKey(Restaurante, on_delete=models.CASCADE, related_name='pratos')
    nome = models.CharField(max_length=255)
    descricao = models.TextField(blank=True, null=True)
    preco_centavos = models.IntegerField()
    calorias_kcal = models.IntegerField(blank=True, null=True)
    proteinas_g = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True)
    carboidratos_g = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True)
    gorduras_g = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True)
    sodio_mg = models.IntegerField(blank=True, null=True)
    eh_vegano = models.BooleanField(default=False)
    eh_vegetariano = models.BooleanField(default=False)
    contem_leite = models.BooleanField(default=False)
    contem_nozes = models.BooleanField(default=False)
    contem_ovo = models.BooleanField(default=False)
    contem_gluten = models.BooleanField(default=False)
    contem_frutos_do_mar = models.BooleanField(default=False)
    contem_soja = models.BooleanField(default=False)
    contem_acucar = models.BooleanField(default=False)
    contem_alcool = models.BooleanField(default=False)
    criado_em = models.DateTimeField(default=timezone.now, editable=False)
    atualizado_em = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.nome
