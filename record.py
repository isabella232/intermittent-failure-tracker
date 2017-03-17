from db import IntermittentsDB

def handler(test_file, platform, builder, number,fail_date):
  db = IntermittentsDB("test.db")
  db.add(test_file,platform,builder,number,fail_date)
