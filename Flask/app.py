import flask

from flask import request

app = flask.Flask("__main__")


@app.route('/form1')
def form1():
    return "form1"


@app.route('/')
def landingPage():
    return flask.render_template('landingPage.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=5992)
