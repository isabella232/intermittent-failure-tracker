from db import IntermittentsDB
import record
import query
import json

def query_test(db, name):
    result = db.query(name)
    if result:
        return result[0]['number']
    return None

db = IntermittentsDB('test_file.json')

assert query_test(db, 'not_so_great.rr') == 19001
assert query_test(db, 'awesome_file.r') == 19000

db.add('another_file.c', 'windows', 'circleci', 1000, "2017-3-16")
assert query_test(db, 'another_file.c') == 1000
db.remove('another_file.c')
assert query_test(db, 'another_file.c') == None

db = IntermittentsDB("test.db")
record.handler('testing_again.c', 'linux', "jenkins3", 2000)
assert query_test(db, 'testing_again.c') == 2000

query.handler("test.db") == "test.db"

print 'All tests passed.'
