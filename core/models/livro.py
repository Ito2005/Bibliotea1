from django.db import models
from .categoria import Categoria
from .editora import Editora
from .autor import Autor
from uploader.models import Image
from rest_framework.serializers import ModelSerializer, SlugRelatedField

from uploader.models import Image
from uploader.serializers import ImageSerializer

class Livro(models.Model):
    titulo = models.CharField(max_length=255)
    isbn = models.CharField(max_length=32, null=True, blank=True)
    quantidade = models.IntegerField(default=0,  null=True, blank=True)
    preco = models.DecimalField(max_digits=7, decimal_places=2, default=0, null=True, blank=True)
    categoria = models.ForeignKey(
        Categoria, on_delete=models.PROTECT, related_name="livros", null=True, blank=True
    )
    editora = models.ForeignKey(Editora, on_delete=models.PROTECT, related_name="livros", null=True, blank=True)
    autores = models.ManyToManyField(Autor, related_name="livros", blank=True)
    capa = models.ForeignKey(
        Image,
        related_name="+",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        default=None,
    )
class LivroSerializer(ModelSerializer):
    capa_attachment_key = SlugRelatedField(
        source="capa",
        queryset=Image.objects.all(),
        slug_field="attachment_key",
        required=False,
        write_only=True,
    )
    capa = ImageSerializer(
        required=False,
        read_only=True
    )

class LivroListRetrieveSerializer(ModelSerializer):
    capa = ImageSerializer(required=False)
    


    def __str__(self):
        return f"({self.id}) {self.titulo} ({self.quantidade})"