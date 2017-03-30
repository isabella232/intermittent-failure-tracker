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
#record
db = IntermittentsDB("test.db")
handlers.record(db, 'testing_again.c', 'linux', "jenkins3", 2000)
assert query_test(db, 'testing_again.c') == 2000
#query
handlers.query(db, "test.db") == "test.db"

#record - don't allow save if any item is blank
#blank test_file
err = ""
try:
    handlers.record(db, '', 'linux', "jenkins3", 2001)
except Exception, e:
    err = str(e)
assert err == "No blank fields"

#blank platform
err = ""
try:
    handlers.record(db, 'test_platform.c', '', "jenkins3", 2002)
except Exception, e:
    err = str(e)
assert err == "No blank fields"

#blank builder
err = ""
try:
    handlers.record(db, 'test_builder.c', 'linux', "", 2003)
except Exception, e:
    err = str(e)
assert err == "No blank fields"

#blank git commit number
err = ""
try:
    handlers.record(db, 'testing_commit.c', 'linux', "jenkins3", "")
except Exception, e:
    err = str(e)
assert err == "No blank fields"

#report success
print 'All tests passed.'
