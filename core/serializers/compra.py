
from rest_framework.serializers import CharField, ModelSerializer
from core.models import Compra, ItensCompra

class ItensCompraCreateUpdateSerializer(ModelSerializer):
    class Meta:
        model = ItensCompra
        fields = ("livro", "quantidade")

class CompraSerializer(ModelSerializer):
    fields = ("id", "usuario", "status", "total", "itens")
    itens = ItensCompraSerializer(many=True, read_only=True)
    usuario = CharField(source="usuario.email", read_only=True) # inclua essa linha
    status = CharField(source="get_status_display", read_only=True) # inclua essa linha
    class Meta:
        model = Compra
        fields = "__all__"

class CompraCreateUpdateSerializer(ModelSerializer):
    itens = ItensCompraCreateUpdateSerializer(many=True) # Aqui mudou

    class Meta:
        model = Compra
        fields = ("usuario", "itens")

    def create(self, validated_data):
        itens_data = validated_data.pop("itens")
        compra = Compra.objects.create(**validated_data)
        for item_data in itens_data:
            ItensCompra.objects.create(compra=compra, **item_data)
        compra.save()
        return compra
    
    
