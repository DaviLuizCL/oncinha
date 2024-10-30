import os
import mongomock


class DevConfig():

    MONGODB_SETTINGS = {
        'db': os.getenv('MONGODB_DB'),
        'host': os.getenv('MONGODB_HOST'),
        'port': os.getenv('MONGODB_PORT'),
        'username': os.getenv('MONGODB_USER'),
        'password': os.getenv('MONGODB_PASSWD')
    }

#TODO -> Configurar para produção
class ProdConfig:
    # MONGO USER
    MS = os.getenv('MONGODB_USER')
    # MONGO_PASSWORD
    MP = os.getenv('MONGODB_PASSWORD')
    # MONGO_HOST
    MH = os.getenv('MONGODB_HOST')
    MONGODB_DB = os.getenv('MONGODB_DB')
    # MONGO APP NAME
    MPN = os.getenv('MONGO_APP_NAME')
    MONGO_URL = os.getenv('MONGO_URL')
    MONGODB_SETTINGS = {
        'host': f"mongodb+srv://{MS}:{MP}@{MH}/?{MPN}=comunidadedevops-python"

    }


class MockConfig:
    TESTING = True
    MONGODB_SETTINGS = {
        'db': 'test',
        'host': 'localhost',
        'port': 27017,
        'mongo_client_class': mongomock.MongoClient 
    }