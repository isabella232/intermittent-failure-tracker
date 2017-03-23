from datetime import datetime

def record(db, test_file, platform, builder, number):
  fail_date = str( datetime.now() )
  if test_file == '' or platform == '' or number == '' or builder == '' :
    raise "No blank fields" 

  db.add(test_file,platform,builder,number,fail_date)

def query(db, filename):
  return db.query(filename)