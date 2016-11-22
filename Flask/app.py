import flask

app = flask.Flask("__main__")

@app.route('/')
def hello():
    return "hello world"

if __name__ == "__main__":
	app.run(host="0.0.0.0", debug=True, port=5992)
