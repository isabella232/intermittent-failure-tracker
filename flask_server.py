from flask import Flask, request, jsonify, render_template, make_response
from db import IntermittentsDB
import handlers
import query
import sys

app = Flask(__name__)
db = IntermittentsDB("./static/intermittent_errors.json")

def request_wants_json():
    best = request.accept_mimetypes \
        .best_match(['application/json', 'text/html'])
    return best == 'application/json' and \
        request.accept_mimetypes[best] > \
        request.accept_mimetypes['text/html']

@app.route("/query.py")
def querypy():
    result = handlers.query(db, request.args.get('filename'))
    return jsonify(result)
    
    if request_wants_json():
        return jsonify(result)
    
    return ('', 200)

@app.route("/record.py", methods=["POST"])
def recordpy():
    try : 
        handlers.record(db, request.form['test_file'], request.form['platform'],request.form['builder'],request.form['number'])
        if request_wants_json() : 
            return make_response(jsonify({ 'status': 'success' }), 204)
        return ('', 204)
    except:
        e = sys.exc_info()[0] 
        if request_wants_json() : 
            return make_response(jsonify({ 'status' : 'failure', 'error': e }), 400)
        return ('', 400) 

@app.route('/query')
def query():
    return render_template('testquery.html')

@app.route('/form')
def form():
    return render_template('testform.html')

@app.route('/file')
def file():
    return app.send_static_file('intermittent_errors.json')

@app.route('/')
def index():
    return render_template('index.html')

def main():
    app.run()

if __name__ == "__main__":
    main()
