#*****************************************
#CSC517 final project
#Spring 2017
#
#Erika Eill eleill@ncsu.edu
#Zachary Taylor zctaylor@ncsu.edu
#Adam Weber acweber2@ncsu.edu
#*****************************************
from db import IntermittentsDB
import handlers
import query
import json

#utility wrapper for unit tests
def query_test(db, name):
    result = db.query(name)
    if result:
        return result[0]['number']
    return None

#set up a temporary db for testing
db = IntermittentsDB('test_file.json')

#Check that numbers come back correct for existing test files
assert query_test(db, 'not_so_great.rr') == 19001
assert query_test(db, 'awesome_file.r') == 19000

#add and check
db.add('another_file.c', 'windows', 'circleci', 1000, "2017-3-16")
assert query_test(db, 'another_file.c') == 1000

#test deletion
db.remove('another_file.c')
assert query_test(db, 'another_file.c') == None

#test handlers record and query methods
db = IntermittentsDB("test.db")
handlers.record(db, 'testing_again.c', 'linux', "jenkins3", 2000)
assert query_test(db, 'testing_again.c') == 2000

handlers.query(db, "test.db") == "test.db"

#report success
print 'All tests passed.'
