#*****************************************
#CSC517 final project
#Spring 2017
#
#Erika Eill eleill@ncsu.edu
#Zachary Taylor zctaylor@ncsu.edu
#Adam Weber acweber2@ncsu.edu
#*****************************************
import json
from tinydb import TinyDB, Query, where
from tinydb.storages import JSONStorage
from tinydb.middlewares import CachingMiddleware

#This is the interface for talking with the json storage format.
class IntermittentsDB:
    #Precondition: a filename for the db file
    #Postcondition: db member of the class is initialized
    def __init__(self, filename):
        self.db = TinyDB(filename)

    
    #Precondition:
    #test_file - the filename of the test file run
    #Postcondition:
    #the json record of the intermittent failures of that test_file
    def query(self, test_file):
        Record = Query()
        return self.db.search(Record.test_file.search(test_file))

    #Precondition:
    #test_file - the filename of the test file run
    #Postcondition:
    #the json records of the intermittent failures of that test_file from within the given range
    def query_range(self, start, end):
        Record = Query()
        return self.db.search((where('fail_date') >= start) & (where('fail_date') <= end))

    #Precondition:
    # test_file - the name of the file that was being tested
    # builder - the platform that was used to run the test
    # number - the github pull request number
    # fail_date - when the failure occurred
    #Postcondition:
    #A record is inserted into the json file
    def add(self, test_file, platform, builder, number, fail_date, fail_time):
        Record = Query()
        self.db.insert({'test_file': test_file, 'platform': platform, 'builder' : builder, 'number' : number, 'fail_date' : fail_date, 'fail_time' : fail_time})
    
    #Precondition:
    #test_file - the name of the test to remove the record for
    #Postcondition:
    #The test_file record no longer exists in the json file
    def remove(self, test_file):
        Record = Query()
        self.db.remove(Record.test_file == test_file)


#Utility method for handling the database
class AutoWriteDB(IntermittentsDB):
    def __init__(self, filename):
        self.filename = filename
        IntermittentsDB.__init__(self, self.filename)

    def __enter__(self):
        return self

    def __exit__(self, etype, evalue, etrace):
        return self
