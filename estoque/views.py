from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Funcionario, Unidade, Saida, Produto, Categoria, Fornecedor, Motivo, SaidaHasProduto
from .serializers import CategoriaSerializer, UnidadeSerializer, FornecedorSerializer, FuncionarioSerializer, MotivoSerializer, ProdutoSerializer, SaidaSerializer, SaidaHasProdutoSerealizer

# Create your views here.
class CategoriaAPIView(APIView):
    def get(self, request):
        categorias = Categoria.objects.all()
        serializer = CategoriaSerializer(categorias, many=True)
        return Response(serializer.data)

    def post(self, reguest):
        serializer = CategoriaSerializer(data=reguest.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class UnidadeAPIView(APIView):
    def get(self, request):
        unidades = Unidade.objects.all()
        serializer = UnidadeSerializer(unidades, many=True)
        return Response(serializer.data)

    def post(self, reguest):
        serializer = UnidadeSerializer(data=reguest.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class FornecedorAPIView(APIView):
    def get(self, request):
        fornecedor = Fornecedor.objects.all()
        serialiser = FornecedorSerializer(fornecedor, many=True)
        return Response(serialiser.data)

    def post(self, reguest):
        serializer = FornecedorSerializer(data=reguest.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class FuncionarioAPIView(APIView):
    def get(self, request):
        funcionario = Funcionario.objects.all()
        serializer = FuncionarioSerializer(funcionario, many=True)
        return Response(serializer.data)

    def post(self, reguest):
        serializer = FuncionarioSerializer(data=reguest.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class MotivoAPIView(APIView):
    def get(self, request):
        motivo = Motivo.objects.all()
        serializer = MotivoSerializer(motivo, many=True)
        return Response(serializer.data)
    
    def post(self, reguest):
        serializer = MotivoSerializer(data=reguest.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class ProdutoAPIView(APIView):
    def get(self, request):
        produtos = Produto.objects.all()
        serializer = ProdutoSerializer(produtos, many=True)
        return Response(serializer.data)
    
    def post(self, reguest):
        serializer = ProdutoSerializer(data=reguest.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class SaidaAPIView(APIView):
    def get(self, request):
        saida = Saida.objects.all()
        serializer = SaidaSerializer(saida, many=True)
        return Response(serializer.data)
    
    def post(self, reguest):
        serializer = SaidaSerializer(data=reguest.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class SaidaHasProdutoAPIView(APIView):
    def get(self, request):
        saidahasproduto = SaidaHasProduto.objects.all()
        serializer = SaidaHasProdutoSerealizer(saidahasproduto, many=True)
        return Response(serializer.data)
    
    def post(self, reguest):
        serializer = SaidaHasProdutoSerealizer(data=reguest.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)