
from flask import jsonify
from flask_restful import Resource, reqparse
from .model import UserModel
from mongoengine import NotUniqueError
from validate_docbr import CPF


_user_parser = reqparse.RequestParser()
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