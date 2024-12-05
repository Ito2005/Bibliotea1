from .autor import AutorSerializer
from .categoria import CategoriaSerializer
from .compra import CompraListSerializer  # novo
from .compra import ItensCompraListSerializer  # novo
from .compra import (
    CompraCreateUpdateSerializer,
    CompraSerializer,
    ItensCompraCreateUpdateSerializer,
    ItensCompraSerializer,
)
from .editora import EditoraSerializer
from .livro import (
    LivroListRetrieveSerializer,
    LivroListSerializer,
    LivroRetrieveSerializer,
    LivroSerializer,
)
from .user import UserSerializer
