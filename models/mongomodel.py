from pymongo import MongoClient

class MongoModel(object):
    def __init__(self, db="test"):
        """
           Initiolisator of mongo object
        """
        self.db_name = db

    def connect_to_db(self):
        """connect to MongoDB database
        """
        try:
            connection = MongoClient(host="mongodb://localhost", port=27017)
            db = connection[self.db_name]
            return db
        except:
            return "Cannot conect to db {}".format(self.db_name)

    def case_collection(self, collection=None):
        """Swith on collection in MongoDB database
        """
        try:
            return self.connect_to_db()[collection]
        except:
            return "Cannot switch on collection {}".format(self.collection)

    def get_data(self):
        pass

    def chack_user(self, name, login):
        

    def add_data(self, collection, document)
        collection = self.case_collection(collection)
        
        try:
            cursor.insert(document, safe=True)
        except:
            "Cannot add data to collection"


if __name__ == "__main__":
    new_connection = MongoModel(db='todolist')
    print new_connection.case_collection(collection='users')
