
from db import IntermittentsDB

def handler(filename):
  db = IntermittentsDB("test.db")
  print(db.query(filename))
