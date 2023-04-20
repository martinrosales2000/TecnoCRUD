#librerias importadas pymongo establece conexion con la base
from pymongo import MongoClient
#esta libreria le brinda seguridad a las inserciones
import certifi

#String de conexion proporcionado por el driver de atlas
MONGO_URI = 'mongodb+srv://martin:Martin1234@clusterdepractica.2gmu7s9.mongodb.net/?retryWrites=true&w=majority'
#MONGO_URI = 'mongodb+srv://augusadmin:1234@clusterdepractica.yfvmtht.mongodb.net/?retryWrites=true&w=majority'
ca = certifi.where()

#funcion de conexion
def dbConnection():
    try:
        client = MongoClient(MONGO_URI, tlsCAFile=ca)
        db = client["dbb_products_app"]
    except ConnectionError:
        print("Error de conexion a la base datos")
    return db