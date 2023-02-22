from classes.DbMongo import DbMongo

class Categoriatienda:
    
    def __init__(self, categoria,id=""):
        self.categoria=categoria,
        self.__id=id,
        self.collection="categoria_tienda"
        
    def save(self, db):
        collection = db[self.__collection]
        result = collection.insert_one(self.__dict__)
        self.__id =  result.inserted_id
        
    @staticmethod
    def get_dict(db):
        collection = db["categoria_tienda"]
        categorias = collection.find()
        dict_categoria_tienda = {}
        for e in categorias:
            dict_categoria_tienda[e["tipo"]] = e["_id"] 