from bottle import Bottle, route, run, template, static_file
from utility import *

app = Bottle()


@app.route('/')
def index():
    panel = Panel('Odin is a Baseball Data Analysis Program Built on Python using Bottle and Bootstrap','Odin','info')
    return template('view/default_container', widget=panel.name, panel_type=panel.type, text=panel.text, title=panel.title)


@app.route('/master')
def master():
    master = getSQLTable('Master')
    print(master)
    table = Table(['Name', 'Birthplace', 'Team'],['Test Player','New York', 'New York Yankees'])
    return template('view/default_container', widget = table.name, fields = table.fields, values= table.data) 


@app.route('/css/<filename>')
def server_static(filename):
    return static_file(filename, root='static/css/')


@app.route('/js/<filename>')
def server_static(filename):
    return static_file(filename, root='static/js/')


class Panel(object):
    def __init__(self, text, title, type):
        self.name       = 'panel'
        self.text       = text
        self.title      = title        
        self.type       = type
        

class Table(object):
    def __init__(self, fields, data):
        self.name       = 'table'
        self.fields     = fields
        self.data       = data
        




    


run(app,debug=True)




