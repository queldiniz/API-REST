# Schema que vai utilizar o marshmallow para serializar e desserializar dados de livros, tanto para enviar quanto para receber a requisicao
from ma import ma 
from models.book import BookModel


class BookSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = BookModel
        load_instance = True  # Permite carregar instâncias do modelo diretamente
        