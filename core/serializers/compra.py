
from rest_framework.serializers import CharField, ModelSerializer
from core.models import Compra, ItensCompra

class ItensCompraSerializer(ModelSerializer):
    class Meta:
        model = ItensCompra
        fields = ("livro", "quantidade")
        depth = 1

class CompraSerializer(ModelSerializer):
    fields = ("id", "usuario", "status", "total", "itens")
    itens = ItensCompraSerializer(many=True, read_only=True)
    usuario = CharField(source="usuario.email", read_only=True) # inclua essa linha
    status = CharField(source="get_status_display", read_only=True) # inclua essa linha
    class Meta:
        model = Compra
        fields = "__all__"
    
    
