import flask
import logging

from flask import request, session, url_for, redirect

app = flask.Flask("__main__")
# TODO Use a secure way to set this
app.secret_key = 'aijdfAJKFJq234kjkdfsa]adfsdfasadfjjq4rjjJHJHjhakgj'


@app.route('/formTest')
def formTest():
    return flask.render_template('formTest.html')


@app.route('/form1validation', methods=['POST'])
def form1validation():
    # TODO don't trust user input, check if we can make this more secure
    session['department'] = request.form['department']
    session['major'] = request.form['major']
    session['minor'] = request.form['minor']
    session['gradYear'] = request.form['gradYear']
    session['CulminatingExp'] = request.form['CulminatingExp']

    for key in session:
        logging.debug("%s: %s" % (key, session[key]))
    return redirect(url_for('form2'))


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
    logging.basicConfig(level=logging.DEBUG)
    app.run(host="0.0.0.0", debug=True, port=5992)
