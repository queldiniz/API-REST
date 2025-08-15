from flask import Flask, Blueprint
from flask_restx import Api

class Server():
    def __init__(self):
        self.app = Flask(__name__)
        self.blueprint = Blueprint('api', __name__, url_prefix='/api')
        self.api = Api(self.blueprint, doc='/doc', title='Sample Flask-SQLAlchemy API')
        self.app.register_blueprint(self.blueprint)

        # configurações do banco de dados
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
        self.app.config['PROPAGATE_EXCEPTIONS'] = True
        self.app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

        # agora chamamos o método corretamente
        self.book_ns = self._book_ns()

    def _book_ns(self):
        return self.api.namespace(
            name='books',
            description='books related operations',
            path='/'
        )

    def run(self):
        self.app.run(
            port=5000,
            debug=True,
            host='0.0.0.0'
        )

server = Server()
