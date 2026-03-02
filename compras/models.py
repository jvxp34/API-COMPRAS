from django.db import models


class Usuario(models.Model):
    nome = models.CharField(max_length=128)
    email = models.EmailField(max_length=100, unique=True)
    senha_hash = models.CharField(max_length=255)
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome


class Product(models.Model):
    nome = models.CharField(max_length=128)

    def __str__(self):
        return self.nome


class ListaCompra(models.Model):
    nome = models.CharField(max_length=255)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='listas')
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)
    total = models.FloatField(default=0)

    def __str__(self):
        return self.nome


class Item(models.Model):
    quantidade = models.FloatField()
    comprado = models.BooleanField(default=False)
    lista = models.ForeignKey(ListaCompra, on_delete=models.CASCADE, related_name='itens')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)
    valor = models.FloatField()

    def __str__(self):
        return f"{self.product.nome} ({self.quantidade})"