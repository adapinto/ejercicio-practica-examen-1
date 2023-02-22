from classes import Tienda, DbMongo, Categoriatienda
from dotenv import load_dotenv

def main():
     client, db = DbMongo.getDB()
    
     #Creamos Categorias
     Categoriatienda("Office").save(db)
     Categoriatienda("Music").save(db)
     Categoriatienda("Electronic").save (db)
     
     
     dictCategorias=Categoriatienda.get_dict(db)
     
     
     tienda=Tienda("La Tiendita","33333333",dictCategorias["Office"])
     tienda.save(db)



     
    
    