from django.urls import path
from .views import CategoriaAPIView, UnidadeAPIView, FornecedorAPIView, FuncionarioAPIView, MotivoAPIView, ProdutoAPIView, SaidaAPIView, SaidaHasProdutoAPIView

urlpatterns = [
    path('categorias/', CategoriaAPIView.as_view(), name='categorias'),
    path('fornecedores/', FornecedorAPIView.as_view(), name='fornecedores'),
    path('funcionarios/', FuncionarioAPIView.as_view(), name='funcionarios'),
    path('motivos/', MotivoAPIView.as_view(), name='motivos'),
    path('produtos/', ProdutoAPIView.as_view(), name='produtos'),
    path('saidas/', SaidaAPIView.as_view(), name='saidas'),
    path('unidades/', UnidadeAPIView.as_view(), name='unidades'),
    path('saidasdeprodutos/', SaidaHasProdutoAPIView.as_view(), name='saidasdeprodutos')
]