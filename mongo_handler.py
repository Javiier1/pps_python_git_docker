from pymongo import MongoClient
import os

def get_mongo_client():
    """Conecta con MongoDB"""
    # Usar nombre del contenedor en lugar de localhost cuando esté en Docker
    mongo_host = os.getenv('MONGO_HOST', 'localhost')
    mongo_port = int(os.getenv('MONGO_PORT', '27017'))
    
    client = MongoClient(mongo_host, mongo_port)
    return client

def get_database():
    """Obtiene la base de datos"""
    client = get_mongo_client()
    db = client['bayeta_db']
    return db

def get_collection():
    """Obtiene la colección de frases"""
    db = get_database()
    collection = db['frases']
    return collection

def inicializar_frases():
    """Inicializa la base de datos con frases desde el archivo frases.txt"""
    collection = get_collection()
    
    # Comprobar si ya hay frases
    if collection.count_documents({}) > 0:
        print("La base de datos ya tiene frases")
        return
    
    # Leer frases del archivo
    try:
        with open('frases.txt', 'r', encoding='utf-8') as f:
            frases = [{"texto": linea.strip()} for linea in f if linea.strip()]
        
        if frases:
            collection.insert_many(frases)
            print(f"Insertadas {len(frases)} frases en la base de datos")
    except FileNotFoundError:
        print("Error: No se encontró el archivo frases.txt")

def consultar_frases_aleatorias(n_frases: int = 1):
    """Consulta N frases aleatorias de la base de datos"""
    collection = get_collection()
    
    # Usar aggregation pipeline para obtener documentos aleatorios
    frases = list(collection.aggregate([
        {"$sample": {"size": n_frases}}
    ]))
    
    return [frase['texto'] for frase in frases]

def insertar_frases(frases_lista):
    """Inserta nuevas frases en la base de datos"""
    collection = get_collection()
    documentos = [{"texto": frase} for frase in frases_lista]
    resultado = collection.insert_many(documentos)
    return len(resultado.inserted_ids)
