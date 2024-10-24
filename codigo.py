from pymongo import MongoClient

# Conecta com o banco de dados
DB = MongoClient("mongodb+srv://admin:admin@projetodb1.nfzqr.mongodb.net/?retryWrites=true&w=majority&appName=ProjetoDB1")

try:
    DB.admin.command('ping')
    print("Conectado com sucesso!\n\n") # Confirma a conexão
    colecoes = DB['Proj1']

    ### Queries ###

except Exception as e:
    print(e)
