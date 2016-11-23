import flask
import logging

from flask import request, session, url_for, redirect

app = flask.Flask("__main__")
# TODO Use a secure way to set this
app.secret_key = 'aijdfAJKFJq234kjkdfsa]adfsdfasadfjjq4rjjJHJHjhakgj'


@app.route('/formTest')
def formTest():
    return flask.render_template('formTest.html')


def logSessionInfo():
    logging.debug("-" * 40)
    for key in session:
        logging.debug("%s: %s" % (key, session[key]))
    logging.debug("-" * 40)


@app.route('/form1validation', methods=['POST'])
def form1validation():
    # TODO don't trust user input, check if we can make this more secure
    # TODO use a iterator
    # TOOD maintain config details separately
    session['department'] = request.form['department']
    session['major'] = request.form['major']
    session['minor'] = request.form['minor']
    session['gradYear'] = request.form['gradYear']
    session['CulminatingExp'] = request.form['CulminatingExp']

    logSessionInfo()
    return redirect(url_for('form2'))


@app.route('/form2validation', methods=['POST'])
def form2validation():
    # TODO don't trust user input, check if we can make this more secure
    # TODO use a iterator
    # TOOD maintain config details separately
    session['OS'] = request.form.get('OS', 0)
    session['DS'] = request.form.get('DS', 0)
    session['OOPS'] = request.form.get('OOPS', 0)
    logSessionInfo()
    return redirect(url_for('form3'))


@app.route('/form1')
def form1():
    # TODO get data from a DB for the from
    # Have hard coded it for now, since we are have limited data
    return flask.render_template('form1.html')


@app.route('/form2')
def form2():
    # TODO use template inheritance to avoid duplicaiton of code
    return flask.render_template('form2.html')


@app.route('/form3')
def form3():
    # TODO use template inheritance to avoid duplicaiton of code
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
