from datetime import datetime

def record(db, test_file, platform, builder, number):
  fail_date = str( datetime.now() )
  db.add(test_file,platform,builder,number,fail_date)

def query(db, filename):
  db.query(filename)