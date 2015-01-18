from bottle import Bottle, route, run, template

app = Bottle()

@app.route('/')
def index():
    return "<h1>Hello World!</h1>"


run(app,debug=True)




