#*****************************************
#CSC517 final project
#Spring 2017
#
#Erika Eill eleill@ncsu.edu
#Zachary Taylor zctaylor@ncsu.edu
#Adam Weber acweber2@ncsu.edu
#*****************************************

from datetime import datetime
from time import gmtime

#Precondition:
#db - the db object that houses the json information
#test_file - the test which has had an intermittent failure
#platform - the machine type on which the test_file was run
#builder - the user that called the run
#number - the github pull request number
#Postcondition:
#The record is added to the database
def record(db, test_file, platform, builder, number):
  fail_date = str( datetime.now().date().strftime("%Y%m%d") )
  fail_time = str( datetime.now().time() )
  if test_file == '' or platform == '' or number == '' or builder == '' :
    raise Exception("No blank fields")

  db.add(test_file,platform,builder,number,fail_date,fail_time)

#Precondition:
#test_file - the name of the test file to find
#Postcondition:
#The json record for that unit test
def query(db, test_file):
  return db.query(test_file)

#Precondition:
#start and end - the date range to use
#Postcondition:
#The json records that fall in that range
def query_range(db, start, end):
  return db.query_range(start,end)
