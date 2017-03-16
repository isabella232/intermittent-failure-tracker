import json
from tinydb import TinyDB, Query
from tinydb.storages import JSONStorage
from tinydb.middlewares import CachingMiddleware

class IntermittentsDB:
    def __init__(self, filename):
        self.db = TinyDB(filename)

    def query(self, test_file):
        Record = Query()
        return self.db.search(Record.test_file.search(test_file))

    def add(self, test_file, platform, builder, number):
        Record = Query()
        if not self.db.search(Record.test_file == test_file):
            self.db.insert({'test_file': test_file, 'platform': platform, 'builder' : builder, 'number' : number})
    
    def remove(self, test_file):
        Record = Query()
        self.db.remove(Record.test_file == test_file)

class AutoWriteDB(IntermittentsDB):
    def __init__(self, filename):
        self.filename = filename
        IntermittentsDB.__init__(self, self.filename)

    def __enter__(self):
        return self

    def __exit__(self, etype, evalue, etrace):
        return self