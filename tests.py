from db import IntermittentsDB
import json

def query(db, name):
    result = db.query(name)
    if result:
        return result[0]['number']
    return None

db = IntermittentsDB('test_file.json')

#These work
assert query(db, 'not_so_great.rr') == 19001
assert query(db, 'awesome_file.r') == 19000

db.add('another_file.c', 'windows', 'circleci', 1000, "2017-3-16")
assert query(db, 'another_file.c') == 1000
db.remove('another_file.c')
assert query(db, 'another_file.c') == None

#These break - what we'll want to do is test the handlers written for the flask_server part.
'''
db.add('foo.html', 12345)
assert query(db, 'foo.html') == 12345
db.remove(12345)
assert query(db, 'foo.html') == None

record.handle('E-easy', 'foo.html', 12345, 'open')
assert query(db, 'foo.html') == None

handlers.on_label_added(db, 'I-intermittent', 'foo.html', 12345, 'open')
assert query(db, 'foo.html') == 12345

handlers.on_label_removed(db, 'E-easy', 'foo.html', 12345, 'open')
assert query(db, 'foo.html') == 12345

handlers.on_label_removed(db, 'I-intermittent', 'foo.html', 12345, 'open')
assert query(db, 'foo.html') == None

handlers.on_label_added(db, 'I-intermittent', 'foo.html', 12345, 'open')
handlers.on_label_added(db, 'C-disabled', 'foo.html', 12345, 'open')
assert query(db, 'foo.html') == None

handlers.on_label_removed(db, 'C-disabled', 'foo.html', 12345, 'open')
assert query(db, 'foo.html') == 12345

handlers.on_issue_updated(db, 'bar.html', 12345, ['I-intermittent'], 'open')
assert query(db, 'foo.html') == None
assert query(db, 'bar.html') == 12345

handlers.on_issue_closed(db, 12345)
assert query(db, 'bar.html') == None

handlers.on_issue_reopened(db, 'bar.html', 12345, ['I-intermittent'])
assert query(db, 'bar.html') == 12345

handlers.on_issue_closed(db, 12345)
assert query(db, 'bar.html') == None

handlers.on_issue_updated(db, 'baz.html', 12345, ['I-intermittent'], 'closed')
assert query(db, 'baz.html') == None

handlers.on_label_removed(db, 'I-intermittent', 'baz.html', 12345, 'closed')
handlers.on_label_added(db, 'I-intermittent', 'baz.html', 12345, 'closed')
handlers.on_label_added(db, 'C-disabled', 'baz.html', 12345, 'closed')

handlers.on_issue_reopened(db, 'baz.html', 12345, ['I-intermittent', 'C-disabled'])
assert query(db, 'bar.html') == None
'''

print 'All tests passed.'
