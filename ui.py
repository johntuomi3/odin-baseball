from bottle import Bottle, route, run, template, static_file
from utility import *

app = Bottle()

# Routes
@app.route('/')
def index():
    panel = Panel('Odin is a Baseball Data Analysis Program Built on Python using Bottle and Bootstrap','Odin','info')
    return template('view/default_container', widget=panel.name, panel_type=panel.type, text=panel.text, title=panel.title)


@app.route('/players')
@app.route('/players/')
def players():
    players = getSQLTable('Master')
    table = Table(players.columns.values.tolist(), players.values)
    return template('view/default_container', widget = table.name, fields = table.fields, data= table.data) 


@app.route('/players/active')
@app.route('/players/active/')
def players():
    players = getSQLTable('Master')
    table = Table(players.columns.values.tolist(), players[(players["finalGame"]>='2013') & (players["deathYear"].isnull()==True)].values)
    return template('view/default_container', widget = table.name, fields = table.fields, data= table.data) 


@app.route('/<teamID>/players/active/hitters')
@app.route('/<teamID>/players/active/hitters/')
def players(teamID):
    players = getSQLTable('Master')
    batters = getSQLTable('Batting')
    roster = players[(players["finalGame"]>='2013') & (players["deathYear"].isnull()==True)].merge(batters[batters["teamID"]==teamID], on='playerID')
    table = Table(roster.columns.values.tolist(), roster.values)
    return template('view/default_container', widget = table.name, fields = table.fields, data= table.data) 


@app.route('/<teamID>/players/active/hitters/<year:int>')
@app.route('/<teamID>/players/active/hitters/<year:int>/')
def players(teamID, year):
    players = getSQLTable('Master')
    batters = getSQLTable('Batting')
    roster = players[(players["finalGame"]>='2013') & (players["deathYear"].isnull()==True)].merge(batters[(batters["teamID"]==teamID) & (batters["yearID"]==year)], on='playerID')
    table = Table(roster.columns.values.tolist(), roster.values)
    return template('view/default_container', widget = table.name, fields = table.fields, data= table.data)


@app.route('/<teamID>/players/active/pitchers')
@app.route('/<teamID>/players/active/pitchers/')
def players(teamID):
    players = getSQLTable('Master')
    pitchers = getSQLTable('Pitching')
    roster = players[(players["finalGame"]>='2013') & (players["deathYear"].isnull()==True)].merge(pitchers[pitchers["teamID"]==teamID], on='playerID')
    table = Table(roster.columns.values.tolist(), roster.values)
    return template('view/default_container', widget = table.name, fields = table.fields, data= table.data) 


@app.route('/<teamID>/players/active/pitchers/<year:int>')
@app.route('/<teamID>/players/active/pitchers/<year:int>/')
def players(teamID, year):
    players = getSQLTable('Master')
    pitchers = getSQLTable('Pitching')
    roster = players[(players["finalGame"]>='2013') & (players["deathYear"].isnull()==True)].merge(pitchers[(pitchers["teamID"]==teamID) & (pitchers["yearID"]==year)], on='playerID')
    table = Table(roster.columns.values.tolist(), roster.values)
    return template('view/default_container', widget = table.name, fields = table.fields, data= table.data) 



@app.route('/teams')
@app.route('/teams/')
def teams():
    teams = getSQLTable('Teams')
    table = Table(teams.columns.values.tolist(), teams.values)
    return template('view/default_container', widget = table.name, fields = table.fields, data= table.data) 


@app.route('/teams/<franchID>')
@app.route('/teams/<franchID>/')
def teams(franchID):
    teams = getSQLTable('Teams')
    table = Table(teams.columns.values.tolist(), teams[teams["franchID"]==franchID].values)
    return template('view/default_container', widget = table.name, fields = table.fields, data= table.data) 


@app.route('/teams/<franchID>/<yearID>')
@app.route('/teams/<franchID>/<yearID>/')
def teams(franchID, yearID):
    teams = getSQLTable('Teams')
    table = Table(teams.columns.values.tolist(), teams[(teams["franchID"]==franchID) & (teams["yearID"]==yearID)].values)
    return template('view/default_container', widget = table.name, fields = table.fields, data= table.data) 


@app.get('/static/js/<filename>')
def javascripts(filename):
    return static_file(filename, root='static/js/')

@app.get('/static/css/<filename>')
def stylesheets(filename):
    return static_file(filename, root='static/css/')


#Web UI Elements
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
        

run(app,debug=True,host='192.168.0.6',port='8080')




