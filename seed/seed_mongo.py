from pymongo import MongoClient


class MongoSeeder:
    def __init__(self):
        host = "mongodb"
        client = MongoClient(host=f"{host}")
        self.__db = client.warehouse

    @property
    def db(self):
        return self.__db

    def seed(self):

        # Clearing collections
        self.__db.warehouse.delete_many({})


        warehouse = []

        
        
        warehouse.append({"type_musique": "POP", "vinyle_musique_disponible": {"titre": "titre1", "artiste": "james brown", "immatriculation": "JB/250/POP/1234"}})

        self.__db.warehouse.insert_many(warehouse)

        cursor = self.__db.warehouse.find()
        for c in cursor:
            print(c)
        


if __name__ == "__main__":
    print("Filling DB")
    MongoSeeder().seed()
    print("Done")
