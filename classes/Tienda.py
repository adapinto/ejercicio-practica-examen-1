from classes.DbMongo import DbMongo
from classes.Categoriatienda import Categoriatienda


class Tienda:
    
    #Definimos constructor
    def __init__(self,nombre,telefono,categoria_tienda,id="" ):
        self.nombre=nombre,
        self.telefono=telefono,
        self.categoria_tienda=categoria_tienda,
        self.__id=id,
        self.collection="tienda"
        
        

        