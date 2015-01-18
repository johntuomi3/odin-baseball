from bottle import Bottle, route, run, template, static_file

app = Bottle()

@app.route('/')
def index():
    panel = Panel('Odin is a Baseball Data Analysis Program Built on Python using Bottle and Bootstrap','Odin','info')
    return template('view/default_container',widget=str(panel.template), panel_type=panel.type, text=panel.text)

@app.route('/css/<filename>')
def server_static(filename):
    return static_file(filename, root='static/css/')

@app.route('/js/<filename>')
def server_static(filename):
    return static_file(filename, root='static/js/')


class Panel(object):
    def __init__(self, text, title, type):
        self.text = text
        self.title = title        
        self.type = type
        self.template = 'view/panel.tpl'

    


run(app,debug=True)




