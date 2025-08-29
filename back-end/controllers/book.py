# controller vai receber as requisicoes e chamar os metodos do model (fazer os tratamentos necessarios)
from flask import request
from flask_restx import Resource, fields
from models.book import BookModel
from schemas.book import BookSchema
from server.instance import server

book_ns = server.book_ns

book_schema = BookSchema()
books_schema = BookSchema(many=True)

item = book_ns.model('Book', {
    'title': fields.String(required=True, description='The title of the book'),
    'pages': fields.Integer(default=0, description='The number of pages in the book'),
})


class Book(Resource):
    def get(self, id):
        book = BookModel.find_by_id(id)
        if book:
            return book_schema.dump(book), 200
        return {'message': 'Book not found'}, 404

    @book_ns.expect(item)
    @book_ns.doc('Update an item')
    def put(self, id):
        book = BookModel.find_by_id(id)
        if not book:
            return {"message": "Book not found"}, 404

        book_json = request.get_json()
        if not book_json:
            return {"message": "No input data provided"}, 400

        # Atualiza apenas os campos enviados
        for key, value in book_json.items():
            setattr(book, key, value)

        book.save_to_db()
        return book_schema.dump(book), 200

    def delete(self, id):
        book = BookModel.find_by_id(id)
        if not book:
            return {"message": "Book not found"}, 404

        book.delete_from_db()
        return {"message": "Book deleted"}, 200


class BookList(Resource):
    def get(self):
        return books_schema.dump(BookModel.find_all()), 200

    @book_ns.expect(item)
    @book_ns.doc('Create an item')
    def post(self):
        book_json = request.get_json()
        if not book_json:
            return {"message": "No input data provided"}, 400

        # Valida e cria objeto BookModel
        book_data = book_schema.load(book_json)
        book_data.save_to_db()

        return book_schema.dump(book_data), 201


# Registrando as rotas
book_ns.add_resource(BookList, "")
book_ns.add_resource(Book, "/<int:id>")

