from flask import Flask, request, jsonify, render_template
import record
app = Flask(__name__)

@app.route("/record.py", methods=["POST"])
def recordpy():
    record.handler(request.form['test_file'], request.form['platform'],request.form['builder'],request.form['number'])
    return ('', 204)

@app.route('/')
def index():
    return render_template('testform.html')

def main():
    app.run()

if __name__ == "__main__":
    main()
