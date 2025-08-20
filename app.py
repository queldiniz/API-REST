from flask import jsonify
from marshmallow import ValidationError

from ma import ma
from db import db
from controllers.book import Book, BookList
from server.instance import server

api = server.api
app = server.app

if __name__ == '__main__':
    # primeiro registra o app no SQLAlchemy e no Marshmallow
    db.init_app(app)
    ma.init_app(app)

    # depois cria as tabelas no contexto do app
    with app.app_context():
        db.create_all()


    api.add_resource(Book,'/books/<int:id>' )
    api.add_resource(BookList, '/books')

   
        # inicia o servidor
    server.run()
