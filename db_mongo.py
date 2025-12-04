from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client['outro_banco']
usuarios = db['usuarios']

usuarios.insert_one({'nome': 'Lucas', 'idade': 26}) # Sempre que eu rodar, ele será adicionado.

for usuario in usuarios.find():
    print(usuario) # {'_id': ObjectId('6931cafc5044ad27eb2b028f'), 'nome': 'Lucas', 'idade': 26}
