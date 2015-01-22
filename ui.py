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


@app.route('/player/<player_name>')
@app.route('/player/<player_name>/')
def playerLooseSearch(player_name):
    player_first_name = str(player_name.split(' ')[0]).title()
    player_last_name = str(player_name.split(' ')[1]).title()
    print(player_first_name, player_last_name)
    players = getSQLTable('Master')
    pitchers = getSQLTable('Pitching')
    batters = getSQLTable('Batting')
    fielders = getSQLTable('Fielding')
    outfielders = getSQLTable('FieldingOF')  
    player = players[(players["nameFirst"]==player_first_name) & (players["nameLast"]==player_last_name)]
    
    hitting_career  = player.merge(batters, on="playerID")
    pitching_career = player.merge(pitchers, on="playerID")
    fielding_career = player.merge(fielders, on="playerID")
    outfielding_career = player.merge(outfielders, on="playerID")
    print(len(hitting_career), len(pitching_career))
    if len(hitting_career) == 0:
        player_selection = pitching_career[["teamID","playerID","nameFirst","nameLast"]]
    elif len(pitching_career) == 0:
        player_selection = hitting_career[["teamID","playerID","nameFirst","nameLast"]] 
    elif len(pitching_career) > 1 and len(hitting_career) > 1:
        player_selection = hitting_career[["teamID","playerID","nameFirst","nameLast"]]
    else:
        player_selection = hitting_career[["teamID","playerID","nameFirst","nameLast"]]  

    player_choice = player_selection.drop_duplicates()
    if len(player_choice) > 1:
        return(player_choice.values.tolist())
    else:
        return(str(hitting_career.values), str(pitching_career.values), str(fielding_career.values), str(outfielding_career.values))


@app.route('/player/<player_name>/<playerID>')
@app.route('/player/<player_name>/<playerID>/')
def player(player_name, playerID):
    player_first_name = str(player_name.split(' ')[0]).title()
    player_last_name = str(player_name.split(' ')[1]).title()
    print(player_first_name, player_last_name)
    players = getSQLTable('Master')
    pitchers = getSQLTable('Pitching')
    batters = getSQLTable('Batting')
    fielders = getSQLTable('Fielding')
    outfielders = getSQLTable('FieldingOF')  
    player = players[(players["nameFirst"]==player_first_name) & (players["nameLast"]==player_last_name) & (players["playerID"]==playerID)]
    hitting_career  = player.merge(batters, on="playerID")
    pitching_career = player.merge(pitchers, on="playerID")
    fielding_career = player.merge(fielders, on="playerID")
    outfielding_career = player.merge(outfielders, on="playerID") 
     
    return(str(hitting_career.values), str(pitching_career.values), str(fielding_career.values), str(outfielding_career.values))


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
        

run(app,debug=True,host='0.0.0.0',port='8080')




