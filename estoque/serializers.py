from rest_framework import serializers
from .models import Funcionario, Unidade, Saida, Produto, Categoria, Fornecedor, Motivo, SaidaHasProduto

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'

class UnidadeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Unidade
        fields = '__all__'

class FornecedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fornecedor
        fields = (
            'nome',
            'cnpj'
        )

class FuncionarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Funcionario
        fields = '__all__'

class MotivoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Motivo
        fields = '__all__'

class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = (
            'nome',
            'valor',
            'unidade',
            'qtd_estoque',
            'categria',
            'fornecedor',
            'observacao'
        )

class SaidaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Saida
        fields = (
            'qtd_produto',
            'data',
            'motivo',
            'funcionario',
            'observacao'
        )

class SaidaHasProdutoSerealizer(serializers.ModelSerializer):
    class Meta:
        model = SaidaHasProduto
        fields = (
            'saida',
            'produto'
        )