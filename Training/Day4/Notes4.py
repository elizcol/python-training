'''
Created on 27 Nov 2014

@author: b8605521
'''
from pymongo.collection import Collection

class Stuff(object):
    def __init__(self, a='a', b='b', c='c'):
        self.a = a
        self.b = b
        self.c = c
    def __str__(self, *args, **kwargs):
        return "<Stuff a='{}', b='{}', c='{}'>".format(self.a, self.b, self.c) 

# create db making table of stuff
from sqlite3 import connect
from contextlib import closing

#note with because using resource
with connect("databaseName") as connection, closing(connection.cursor()) as cursor:
    cursor.execute('create table stuff(a text, b text, c text)')

# for insert, change the execute code to insert into stuff ... and the connection.commit after cursor finished
# reading from db
with connect("databaseName") as connection:
    with closing(connection.cursor()) as cursor:
        values = [Stuff(*row) for row in cursor.execute('select * from stuff')]
    print('all values')
    for v in values:
        print(str(v))
        
# use alchemy for a layer
from sqlalchemy import create_engine, MetaData, Table

engine = create_engine('sqlite///' + 'dbName')
stuffTable = Table('stuffTable', MetaData(), autoload = True, autoload_with=engine)
for value in (Stuff(*result) for result in engine.execute(stuffTable.select(stuffTable.c.a == 'y'))):#see the python where clause instead of sql
    print(str(value))       


#pymongo
from pymongo import MongoClient

values = (
          Stuff('x','a','b'),
          Stuff('y','aa','bb'),
          Stuff('z','aaa','bbb'))

collection = MongoClient('''url''').stuffDatabase.stuffCollection
#insert
for v in values:
    collection.insert({'a': value.a, 'b': value.b, 'c': value.c})
    print(str(v))
#query
for v in collection.find({'a':'y'}):
    print(str(v))
# delete db
MongoClient().drop_database("sillyDB")

'''
django
cmd line:
django-admin startproject ProjName
python3 manage.py migrate
python3 manage.py [arg] (eg runserver)
when running can go into admin. no user yet. run cmd with createsuperuser



pyland - game to learn python


selenium - the finalizer makes sure ff quits when it finishes running the test

def browser(request):
    firefox = webdriver.Firefox()
    request.addfinalizer(lambda: firefox.quit())
    return firefox
'''
