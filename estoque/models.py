from django.db import models

# Create your models here.
class Categoria(models.Model):
    nome = models.CharField(max_length=100)

    class Meta:
        verbose_name = ("Categoria")
        verbose_name_plural = ("Categorias")

    def __str__(self):
        return self.nome
    
class Unidade(models.Model):
    nome = models.CharField(max_length=90)

    class Meta:
        verbose_name = ("Unidade")
        verbose_name_plural = ("Unidades")
    
    def __str__(self):
        return self.nome

class Fornecedor(models.Model):
    nome = models.CharField(max_length=100)
    cnpj = models.IntegerField()
    
    class Meta:
        verbose_name = "Fornecedor"
        verbose_name_plural = "Fornecedores"

    def __str__(self):
        return self.nome
    
class Funcionario(models.Model):
    nome = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Funcionario"
        verbose_name_plural = "Funcionarios"

    def __str__(self):
        return self.nome

class Motivo(models.Model):
    motivo = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Motivo"
        verbose_name_plural = "Motivos"

    def __str__(self):
        return self.motivo

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    valor = models.IntegerField()
    qtd_estoque = models.IntegerField()
    unidade = models.ForeignKey(Unidade, on_delete=models.CASCADE)
    categria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    fornecedor = models.ForeignKey(Fornecedor, on_delete=models.CASCADE)
    observacao = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = "Produto"
        verbose_name_plural = "Produtos"

    def __str__(self):
        return self.nome

class Saida(models.Model):
    qtd_produto = models.IntegerField()
    data = models.DateField()
    motivo = models.ForeignKey(Motivo, on_delete=models.CASCADE)
    funcionario = models.ForeignKey(Funcionario, on_delete=models.CASCADE)
    observacao = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = "Saida"
        verbose_name_plural = "Saidas"

class SaidaHasProduto(models.Model):
    saida = models.ForeignKey(Saida, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)

    class Meta:
        unique_together = ['saida', 'produto']