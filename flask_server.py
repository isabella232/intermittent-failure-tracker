from flask import Flask, request, jsonify
from . import record
app = Flask(__name__)

@app.route("/record.py", methods=["POST"])
def recordpy():
    record.handler(request.form.get('payload', '{}'))
    return ('', 204)

@app.route('/')
def index():
    return "Hi!"

def main():
    app.run()

if __name__ == "__main__":
    main()
