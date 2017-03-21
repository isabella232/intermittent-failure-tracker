from db import IntermittentsDB
from datetime import datetime

def handler(test_file, platform, builder, number):
  fail_date = str( datetime.now() )
  db = IntermittentsDB("test.db")
  db.add(test_file,platform,builder,number,fail_date)
