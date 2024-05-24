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

class CategoriaAPIViewID(APIView):
    def get(self, request, id):
        categoria = Categoria.objects.get(pk=id)
        serializer = CategoriaSerializer(categoria)
        return Response(serializer.data)

    def put(self, request, id):
        categoria = Categoria.objects.get(pk=id)
        serializer = CategoriaSerializer(categoria, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def delete(self, request, id):
        categoria = Categoria.objects.get(pk=id)
        categoria.delete()
        return Response(status=status.HTTP_200_OK)

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

class UnidadeAPIViewID(APIView):
    def get(self, request, id):
        unidade = Unidade.objects.get(pk=id)
        serializer = UnidadeSerializer(unidade)
        return Response(serializer.data)

    def put(self, request, id):
        unidade = Unidade.objects.get(pk=id)
        serializer = UnidadeSerializer(unidade, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def delete(self, request, id):
        unidade = Unidade.objects.get(pk=id)
        unidade.delete()
        return Response(status=status.HTTP_200_OK)

class FornecedorAPIView(APIView):
    def get(self, request):
        fornecedores = Fornecedor.objects.all()
        serialiser = FornecedorSerializer(fornecedores, many=True)
        return Response(serialiser.data)

    def post(self, reguest):
        serializer = FornecedorSerializer(data=reguest.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
class FornecedorAPIViewID(APIView):
    def get(self, request, id):
        fornecedor = Fornecedor.objects.get(pk=id)
        serializer = FornecedorSerializer(fornecedor)
        return Response(serializer.data)

    def put(self, request, id):
        fornecedor = Fornecedor.objects.get(pk=id)
        serializer = FornecedorSerializer(fornecedor, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def delete(self, request, id):
        fornecedor = Fornecedor.objects.get(pk=id)
        fornecedor.delete()
        return Response(status=status.HTTP_200_OK)

class FuncionarioAPIView(APIView):
    def get(self, request):
        funcionarios = Funcionario.objects.all()
        serializer = FuncionarioSerializer(funcionarios, many=True)
        return Response(serializer.data)

    def post(self, reguest):
        serializer = FuncionarioSerializer(data=reguest.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class FuncionarioAPIViewID(APIView):
    def get(self, request, id):
        funcionario = Funcionario.objects.get(pk=id)
        serializer = FuncionarioSerializer(funcionario)
        return Response(serializer.data)

    def put(self, request, id):
        funcionario = Funcionario.objects.get(pk=id)
        serializer = FuncionarioSerializer(funcionario, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def delete(self, request, id):
        funcionario = Funcionario.objects.get(pk=id)
        funcionario.delete()
        return Response(status=status.HTTP_200_OK)

class MotivoAPIView(APIView):
    def get(self, request):
        motivos = Motivo.objects.all()
        serializer = MotivoSerializer(motivos, many=True)
        return Response(serializer.data)
    
    def post(self, reguest):
        serializer = MotivoSerializer(data=reguest.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class MotivoAPIViewID(APIView):
    def get(self, request, id):
        motivo = Motivo.objects.get(pk=id)
        serializer = MotivoSerializer(motivo)
        return Response(serializer.data)

    def put(self, request, id):
        motivo = Motivo.objects.get(pk=id)
        serializer = MotivoSerializer(motivo, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def delete(self, request, id):
        motivo = Motivo.objects.get(pk=id)
        motivo.delete()
        return Response(status=status.HTTP_200_OK)

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
    
class ProdutoAPIViewID(APIView):
    def get(self, request, id):
        produto = Produto.objects.get(pk=id)
        serializer = ProdutoSerializer(produto)
        return Response(serializer.data)

    def put(self, request, id):
        produto = Produto.objects.get(pk=id)
        serializer = ProdutoSerializer(produto, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def delete(self, request, id):
        produto = Produto.objects.get(pk=id)
        produto.delete()
        return Response(status=status.HTTP_200_OK)

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

class SaidaAPIViewID(APIView):
    def get(self, request, id):
        saida = Saida.objects.get(pk=id)
        serializer = SaidaSerializer(saida)
        return Response(serializer.data)

    def put(self, request, id):
        saida = Saida.objects.get(pk=id)
        serializer = SaidaSerializer(saida, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def delete(self, request, id):
        saida = Saida.objects.get(pk=id)
        saida.delete()
        return Response(status=status.HTTP_200_OK)

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

class SaidaHasProdutoAPIViewID(APIView):
    def get(self, request, id):
        saidahasproduto = SaidaHasProduto.objects.get(pk=id)
        serializer = SaidaHasProdutoSerealizer(saidahasproduto)
        return Response(serializer.data)

    def put(self, request, id):
        saidahasproduto = SaidaHasProduto.objects.get(pk=id)
        serializer = SaidaHasProdutoSerealizer(saidahasproduto, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def delete(self, request, id):
        saidahasproduto = SaidaHasProduto.objects.get(pk=id)
        saidahasproduto.delete()
        return Response(status=status.HTTP_200_OK)