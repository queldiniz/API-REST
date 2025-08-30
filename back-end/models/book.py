from db import db

class BookModel(db.Model):
    __tablename__ = 'books'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False, unique=True)
    pages = db.Column(db.Integer, nullable=False)
    author = db.Column(db.String(80), nullable=True)

    def __init__(self, title, pages, author):
        self.title = title
        self.pages = pages
        self.author = author

    def __repr__(self):
        return f'BookModel(title={self.title}, pages={self.pages}, author={self.author})'

    def json(self, ):
        return {
            'title': self.title,
            'pages': self.pages,
            'author': self.author
        }
    
    # metodos da classe BookModel
    @classmethod
    def find_by_title(cls, title):
        return cls.query.filter_by(title=title).first()
    
    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(id=id).first()
    
    # para pegar todos os dados do bd
    @classmethod
    def find_all(cls):
        return cls.query.all()
    

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()