from .db import db


class UserModel(db.Document):
    cpf = db.StringField(required=True, unique=True)
    email = db.EmailField(required=True)
    first_name = db.StringField(max_length=50, required=True)
    last_name = db.StringField(max_length=50, required=True)
    birth_date = db.DateTimeField(required=True)

#Criação do animal no banco de dados
class AnimalModel(db.Document):
    code = db.IntField(required=True, unique=True)
    name = db.StringField(required=True)
    multiplicator = db.DecimalField(required=True, precision=2)
    photo = db.StringField(required=True)
