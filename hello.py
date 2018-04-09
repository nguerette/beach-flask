import os
from flask import Flask
app = Flask(__name__)


@app.route("/")
def hello():
    resp = app.make_response("Hello Furld!")
    resp.headers['Content-Type'] = 'text/plain; charset=utf-8'
    return resp


try:
    port = int(os.getenv('PORT'))
except (TypeError, ValueError):
    port = 5000

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=port)
