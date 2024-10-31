
from flask import jsonify
from flask_restful import Resource, reqparse
from .model import UserModel, AnimalModel
from mongoengine import NotUniqueError
from validate_docbr import CPF


_user_parser = reqparse.RequestParser()
_animal_parser = reqparse.RequestParser()
_user_parser.add_argument('first_name',
                          type=str,
                          required=True,
                          help="This field cannot be blank")
_user_parser.add_argument('last_name',
                          type=str,
                          required=True,
                          help="This field cannot be blank")
_user_parser.add_argument('cpf',
                          type=str,
                          required=True,
                          help="This field cannot be blank")
_user_parser.add_argument('email',
                          type=str,
                          required=True,
                          help="This field cannot be blank")
_user_parser.add_argument('birth_date',
                          type=str,
                          required=True,
                          help="This field cannot be blank")
#Tradução do JSON para arquivo do banco
_animal_parser.add_argument('code',
                          type=int,
                          required=True,
                          help="This field cannot be blank")
_animal_parser.add_argument('name',
                          type=str,
                          required=True,
                          help="This field cannot be blank")
_animal_parser.add_argument('multiplicator',
                          type=float,
                          required=True,
                          help="This field cannot be blank")
_animal_parser.add_argument('photo',
                          type=str,
                          required=True,
                          help="This field cannot be blank")


cpf = CPF()


class Users(Resource):
    def get(self):
        return jsonify(UserModel.objects())


class User(Resource):
    def post(self):
        data = _user_parser.parse_args()
        if not cpf.validate(data["cpf"]):
            return {"message": "CPF is invalid!"}, 400

        try:

            response = UserModel(**data).save()
            return {"message": f"user {response.id} successfully created!"}

        except NotUniqueError:
            return {"message": "CPF already exists in database"}, 400

    def get(self, cpf):
        response = UserModel.objects(cpf=cpf)
        if response:

            return jsonify(response)
        return {"message": "User does not exist in database"}, 400
    
#Função executada quando existem requisições na url /animals
class Animals(Resource):
    def post(self):
        data = _animal_parser.parse_args()
        response = AnimalModel(**data).save()
        return {"message": f"Animal {response.name} successfully created!"}
    def get(self):
        return jsonify(AnimalModel.objects())

# class Animal(Resource):
#     def post(self):
#         return 0
#     def get(self):
#         return jsonify(AnimalModel.objects())
#     def get(self, code):
#         response = AnimalModel.objects(code=code)
#         if response:

#             return jsonify(response)
#         return {"message": "Animal does not exist in database"}, 400
