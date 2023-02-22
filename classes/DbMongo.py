import pymongo
import os

class DbMongo:

    @staticmethod
    def getDB():
        user = 'Adimari'
        password = '99725478Adimari'
        cluster = 'poounahclase3.v7p4vxg.mongodb.net'
        user = os.environ['USER']
        password = os.environ['PASSWORD']
        cluster = os.environ['CLUSTER']
        query_string = 'retryWrites=true&w=majority'


        ## Connection String
        uri = "mongodb+srv://{0}:{1}@{2}/?{3}".format(
            user
            , password
            , cluster
            , query_string
        )

        client = pymongo.MongoClient(uri)
        db = client['unah']
        db = client[os.environ['DB']]

        return db
        return client, db