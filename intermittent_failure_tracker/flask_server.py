#*****************************************
#CSC517 final project
#Spring 2017
#
#Erika Eill eleill@ncsu.edu
#Zachary Taylor zctaylor@ncsu.edu
#Adam Weber acweber2@ncsu.edu
#Preston Scott pdscott2@ncsu.edu
#*****************************************
from flask import Flask, request, jsonify, render_template, make_response, abort, send_from_directory
from db import IntermittentsDB
import handlers
import sys
import json
import os

app = Flask(__name__)
db = IntermittentsDB("intermittent_errors.json")

#utility method
def request_wants_json():
    best = request.accept_mimetypes \
        .best_match(['application/json', 'text/html'])
    return best == 'application/json' and \
        request.accept_mimetypes[best] > \
        request.accept_mimetypes['text/html']

#rest endpoint for handling the query of data
@app.route("/query.py")
def querypy():
    result = handlers.query(db, request.args.get('filename'))
    return jsonify(result)
    
    if request_wants_json():
        return jsonify(result)
    
    return ('', 200)

@app.route("/query_range.py")
def queryRange():
    result = handlers.query_range(db, request.args.get('start'), request.args.get('end'))
    return jsonify(result)
    
    if request_wants_json():
        return jsonify(result)
    
    return ('', 200)

#rest end point for handling addition of data
@app.route("/record.py", methods=["POST"])
def recordpy():
    try :
        handlers.record(db, request.form['test_file'], request.form['platform'],request.form['builder'],request.form['number'])
        if request_wants_json() :
            return make_response(jsonify({ 'status': 'success' }), 200)
        return ('', 204)
    except:
        e = sys.exc_info()[0] 
        if request_wants_json() :
            return make_response(jsonify({ 'status' : 'failure', 'error': e }), 400)
        abort(400) 

#request for the form for getting records from the db
@app.route('/query')
def query():
    return render_template('testquery.html')

#request for the form for getting records from the db by range
@app.route('/query_range')
def query_range():
    return render_template('testqueryrange.html')

#endpoint for production front end - serves form for getting records from the db by name and date range
@app.route("/search")
def search():   
    if request.args.get('isQuery') :
        if request.args.get('dateCheck') :
          result = handlers.adv_query(db, request.args.get('filename'), request.args.get('start'), request.args.get('end'))
        else :
          result = handlers.adv_query(db, request.args.get('filename'), request.args.get('defaultStart'), request.args.get('defaultEnd')) 
        return render_template('searchtool.html', records=result)
    else :
        return render_template('searchtool.html')

#request for loading the testing form for adding records
@app.route('/form')
def form():
    return render_template('testform.html')

#file dump for inspecting the database
@app.route('/file')
def file():
    return send_from_directory(os.getcwd(), 'intermittent_errors.json')

#default loading page for testing forms
@app.route('/')
def index():
    return render_template('index.html')

#error handler
@app.errorhandler(400)
def page_not_found(e):
    return render_template('error.html'), 404

#Main section
def main(port=None):
    with open('config.json') as f:
        config = json.loads(f.read())
        assert('port' in config)
    app.run(port=config['port'])

if __name__ == "__main__":
    main()
