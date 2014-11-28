'''
Created on 27 Nov 2014

@author: b8605521
'''
from pymongo.mongo_client import MongoClient

class Contact(object):
    def __init__(self, firstName, lastName, email):
        self.firstName = firstName
        self.lastName = lastName
        self.email = email
    def __str__(self):
        return "{firstName:'{}', lastName:'{}', email:'{}'}".format(self.firstName, self.lastName, self.email) 

class ContactsMongo(object):
    
    def initialise(self, values):
        collection = MongoClient("localhost").contactDatabase.contactCollection
        for v in values:
            collection.insert({'firstName' : v.firstName, 'lastName': v.lastName, 'email': v.email})
            print('Inserted: ' + str(v))
    
    def getAllDocs(self):
        collection = MongoClient("localhost").contactDatabase.contactCollection
        print("find all documents")
        for v in collection.find():
            print('\t' + str(v))
    
    def getByFirstName(self, firstName):
        collection = MongoClient("localhost").contactDatabase.contactCollection
        for v in collection.find({'firstName':firstName}):
            print('matched: ' + str(v))
    
    def updateByFirstName(self, firstName, new):
        collection = MongoClient("localhost").contactDatabase.contactCollection
        print("update: " + new.email)
        collection.update({'firstName' : firstName}, {"$set" :{'firstName' : new.firstName, 'lastName': new.lastName, 'email': new.email}})
    
    def dropDB(self):
        MongoClient("localhost").drop_database("contactDatabase")
        print('dropped contactDB')
    
if __name__ == '__main__':
    contactMongo = ContactsMongo()
    values = (
              Contact('Fred','Flintstone','fred@rocks.com'),
              Contact('Wilma','Flintstone','wilma@rocks.com'),
              Contact('Pebbles','Flintstone','pebbles@rocks.com')
              )
    #contactMongo.initialise(values)
    #contactMongo.dropDB()
    contactMongo.getAllDocs()
    contactMongo.getByFirstName('Fred')
    updateCon = Contact('Fred','Flintstone','fred.test@rocks.co.uk')
    contactMongo.updateByFirstName("Fred" , updateCon)
    contactMongo.getAllDocs()