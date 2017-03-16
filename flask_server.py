from flask import Flask, request, jsonify, render_template
import record
import query
app = Flask(__name__)

@app.route("/query.py", methods=["POST"])
def querypy():
    query.handler(request.form['filename'])
    return ('', 204)

@app.route("/record.py", methods=["POST"])
def recordpy():
    record.handler(request.form['test_file'], request.form['platform'],request.form['builder'],request.form['number'],request.form['fail_date'])
    return ('', 204)

@app.route('/doquery')
def querytime():
    return render_template('testquery.html')

@app.route('/')
def index():
    return render_template('testform.html')

def main():
    app.run()

if __name__ == "__main__":
    main()
