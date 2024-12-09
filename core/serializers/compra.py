from core.models import Compra, ItensCompra
from rest_framework.serializers import (
    CharField,
    CurrentUserDefault,
    HiddenField,
    ModelSerializer,
    SerializerMethodField,
    ValidationError, # novo
)

class ItensCompraCreateUpdateSerializer(ModelSerializer):
    class Meta:
        model = ItensCompra
        fields = ("livro", "quantidade")

    def validate(self, item):
        if item["quantidade"] > item["livro"].quantidade:
            raise ValidationError("Quantidade de itens maior do que a quantidade em estoque.")
        return item


class ItensCompraListSerializer(ModelSerializer):
    livro = CharField(source="livro.titulo", read_only=True)

    class Meta:
        model = ItensCompra
        fields = ("quantidade", "livro")
        depth = 1


class ItensCompraSerializer(ModelSerializer):
    total = SerializerMethodField()

    def get_total(self, instance):
        return instance.livro.preco * instance.quantidade

    class Meta:
        model = ItensCompra
        fields = ("quantidade", "total", "livro")
        depth = 1


class CompraCreateUpdateSerializer(ModelSerializer):
    usuario = HiddenField(default=CurrentUserDefault())
    itens = ItensCompraCreateUpdateSerializer(many=True)  # Aqui mudou

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


class CompraListSerializer(ModelSerializer):
    usuario = CharField(source="usuario.email", read_only=True)
    itens = ItensCompraListSerializer(many=True, read_only=True)

    class Meta:
        model = Compra
        fields = ("id", "usuario", "itens")


class CompraSerializer(ModelSerializer):
    itens = ItensCompraSerializer(many=True, read_only=True)
    usuario = CharField(source="usuario.email", read_only=True)  # inclua essa linha
    status = CharField(source="get_status_display", read_only=True)  # inclua essa linha

    class Meta:
        model = Compra
        fields = ("id", "usuario", "status", "total", "itens")
