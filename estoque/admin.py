from django.contrib import admin
from .models import Funcionario, Unidade, Saida, Produto, Categoria, Fornecedor, Motivo, SaidaHasProduto

# Register your models here.
@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['nome']

@admin.register(Unidade)
class UnidadeAdmin(admin.ModelAdmin):
    list_display = ['nome']

@admin.register(Fornecedor)
class FornecedorAdmin(admin.ModelAdmin):
    list_display = ['nome', 'cnpj']

@admin.register(Funcionario)
class FuncionarioAdmin(admin.ModelAdmin):
    list_display = ['nome']

@admin.register(Motivo)
class MotivoAdmin(admin.ModelAdmin):
    list_display = ['motivo']

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'valor', 'unidade', 'qtd_estoque', 'categria', 'fornecedor', 'observacao']

@admin.register(Saida)
class SaidaAdmin(admin.ModelAdmin):
    list_display = ['qtd_produto', 'data', 'motivo', 'funcionario', 'observacao']

@admin.register(SaidaHasProduto)
class SaidaHasProdutoAdmin(admin.ModelAdmin):
    list_display = ['saida', 'produto']