import flask
from flask import redirect, url_for

app = flask.Flask("__main__")


@app.route('/')
def hello():
    return flask.render_template('index.html', name='mak')


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=5992)
