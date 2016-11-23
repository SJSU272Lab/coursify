import flask

from flask import request

app = flask.Flask("__main__")


@app.route('/form1')
def form1():
    return flask.render_template('form1.html')


@app.route('/form2')
def form2():
    return flask.render_template('form2.html')


@app.route('/feedback')
def feedback():
    return flask.render_template('feedback.html')


@app.route('/')
def landingPage():
    return flask.render_template('landingPage.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=5992)
