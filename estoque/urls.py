from django.urls import path
from .views import (
        CategoriaAPIView, 
        CategoriaAPIViewID, 
        UnidadeAPIView, 
        UnidadeAPIViewID, 
        FornecedorAPIView, 
        FornecedorAPIViewID, 
        FuncionarioAPIView,
        FuncionarioAPIViewID,
        MotivoAPIView,
        MotivoAPIViewID,
        ProdutoAPIView,
        ProdutoAPIViewID,
        SaidaAPIView,
        SaidaAPIViewID,
        SaidaHasProdutoAPIView,
        SaidaHasProdutoAPIViewID
    )

urlpatterns = [
    path('categorias/', CategoriaAPIView.as_view(), name='categorias'),
    path('categoria/<int:id>/', CategoriaAPIViewID.as_view(), name='categoria'),
    path('fornecedores/', FornecedorAPIView.as_view(), name='fornecedores'),
    path('fornecedor/<int:id>/', FornecedorAPIViewID.as_view(), name='fornecedor'),
    path('funcionarios/', FuncionarioAPIView.as_view(), name='funcionarios'),
    path('funcionario/<int:id>/', FuncionarioAPIViewID.as_view(), name='funcionario'),
    path('motivos/', MotivoAPIView.as_view(), name='motivos'),
    path('motivo/<int:id>/', MotivoAPIViewID.as_view(), name='motivo'),
    path('produtos/', ProdutoAPIView.as_view(), name='produtos'),
    path('produto/<int:id>/', ProdutoAPIViewID.as_view(), name='produto'),
    path('saidas/', SaidaAPIView.as_view(), name='saidas'),
    path('saida/<int:id>/', SaidaAPIViewID.as_view(), name='saida'),
    path('unidades/', UnidadeAPIView.as_view(), name='unidades'),
    path('unidade/<int:id>/', UnidadeAPIViewID.as_view(), name='unidade'),
    path('saidasdeprodutos/', SaidaHasProdutoAPIView.as_view(), name='saidasdeprodutos'),
    path('saidasdeproduto/<int:id>/', SaidaHasProdutoAPIViewID.as_view(), name='saidasdeproduto')
]