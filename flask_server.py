from flask import Flask, request, jsonify, render_template
from db import IntermittentsDB
import handlers
import query
import os.path

app = Flask(__name__)
db = IntermittentsDB("./static/intermittent_errors.json")

@app.route("/query.py", methods=["POST"])
def querypy():
    handlers.query(db, request.form['filename'])
    return ('', 204)

@app.route("/record.py", methods=["POST"])
def recordpy():
    handlers.record(db, request.form['test_file'], request.form['platform'],request.form['builder'],request.form['number'])
    return ('', 204)

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
