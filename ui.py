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
    player_sql = """
                    SELECT "Master"."playerID"
                           ,CASE WHEN "Batting"."teamID" IS NULL
                                 THEN "Pitching"."teamID"
                                 ELSE "Batting"."teamID"
                                 END                    teamID
                    FROM "Master"
                    LEFT JOIN "Pitching"
	                    ON "Master"."playerID" = "Pitching"."playerID"
                    LEFT JOIN "Batting"
	                    ON "Master"."playerID" = "Batting"."playerID"
                    WHERE 
	                    "Master"."nameFirst" = '%s'
                             AND "Master"."nameLast" = '%s'
                 """ %(player_first_name, player_last_name)
    batting_sql = """
                    SELECT "yearID",
                           "G", 
                           "AB", 
                           "R", 
                           "H", 
                           "2B", 
                           "3B", 
                           "HR", 
                           "RBI", 
                           "SB", 
                           "CS", 
                           "BB", 
                           "SO", 
                           "IBB",
                           "HBP",
                           "SH",
                           "SF",
                           "GIDP"
                    FROM "Master"
                    JOIN "Batting"
	                    ON "Master"."playerID" = "Batting"."playerID"
                    WHERE 
	                    "Master"."nameFirst" = '%s'
                             AND "Master"."nameLast" = '%s'
                  """ %(player_first_name, player_last_name)


    pitching_sql = """
                    SELECT "yearID",
                           "W", 
                           "L", 
                           "G", 
                           "GS", 
                           "CG", 
                           "SHO", 
                           "SV", 
                           "IPouts", 
                           "H", 
                           "ER", 
                           "HR", 
                           "BB", 
                           "SO",
                           "BAOpp",
                           "ERA",
                           "IBB",
                           "WP",
                           "HBP",
                           "BK",
                           "BFP",
                           "GF",
                           "R",
                           "SH",
                           "SF",
                           "GIDP"
                    FROM "Master"
                    JOIN "Pitching"
	                    ON "Master"."playerID" = "Pitching"."playerID"
                    WHERE 
	                    "Master"."nameFirst" = '%s'
                             AND "Master"."nameLast" = '%s'
                  """ %(player_first_name, player_last_name)

    fielding_sql = """
                    SELECT "yearID",
                           "POS", 
                           "G", 
                           "GS", 
                           "InnOuts", 
                           "PO", 
                           "A", 
                           "E", 
                           "DP", 
                           "PB", 
                           "WP", 
                           "SB", 
                           "CS", 
                           "ZR"
                    FROM "Master"
                    JOIN "Fielding"
	                    ON "Master"."playerID" = "Fielding"."playerID"
                    WHERE 
	                    "Master"."nameFirst" = '%s'
                             AND "Master"."nameLast" = '%s'
                  """ %(player_first_name, player_last_name)

    outfielding_sql = """
                    SELECT "yearID",
                           "Glf", 
                           "Gcf", 
                           "Grf" 
                    FROM "Master"
                    JOIN "FieldingOF"
	                    ON "Master"."playerID" = "FieldingOF"."playerID"
                    WHERE 
	                    "Master"."nameFirst" = '%s'
                             AND "Master"."nameLast" = '%s'
                  """ %(player_first_name, player_last_name)
    player_selection = pd.read_sql_query(player_sql, engine)
    hitting_career = pd.read_sql_query(batting_sql, engine)
    pitching_career = pd.read_sql_query(pitching_sql, engine)
    fielding_career = pd.read_sql_query(fielding_sql, engine)
    outfielding_career = pd.read_sql_query(outfielding_sql, engine)


    player_choice = player_selection.drop_duplicates()
    print(player_choice)
    if len(player_choice) > 1:
        html_string = "<ul>"
        for i in player_choice.values.tolist():
            html_string +=("<li><a href=\"/player/"+ player_name +"/" + i[0]+"\">" + i[1]  + " " + str(player_name).title() + "</a></li>")
        html_string += "</ul>"
        print(html_string)
        panel = Panel(html_string,'Multiple Players Found','warning')
        return template('view/default_container', widget=panel.name, panel_type=panel.type, text=panel.text, title=panel.title)
        
    else:
        widget_list = []
        hitting_table = Table(hitting_career.columns.values.tolist(), hitting_career.values)
        pitching_table = Table(pitching_career.columns.values.tolist(), pitching_career.values)
        fielding_table = Table(fielding_career.columns.values.tolist(), fielding_career.values)
        outfielding_table = Table(outfielding_career.columns.values.tolist(), outfielding_career.values)
        widget_list.append(hitting_table)
        widget_list.append(pitching_table)
        widget_list.append(fielding_table)
        widget_list.append(outfielding_table)
        return template('view/player_page', widgets=widget_list)


@app.route('/player/<player_name>/<playerID>')
@app.route('/player/<player_name>/<playerID>/')
def player(player_name, playerID):
    player_first_name = str(player_name.split(' ')[0]).title()
    player_last_name = str(player_name.split(' ')[1]).title()
    #print(player_first_name, player_last_name)
    batting_sql = """
                    SELECT "yearID",
                           "G", 
                           "AB", 
                           "R", 
                           "H", 
                           "2B", 
                           "3B", 
                           "HR", 
                           "RBI", 
                           "SB", 
                           "CS", 
                           "BB", 
                           "SO", 
                           "IBB",
                           "HBP",
                           "SH",
                           "SF",
                           "GIDP"
                    FROM "Master"
                    JOIN "Batting"
	                    ON "Master"."playerID" = "Batting"."playerID"
                    WHERE 
	                    "Master"."nameFirst" = '%s'
                             AND "Master"."nameLast" = '%s'
                             AND "Master"."playerID" = '%s'
                  """ %(player_first_name, player_last_name, playerID)


    pitching_sql = """
                    SELECT "yearID",
                           "W", 
                           "L", 
                           "G", 
                           "GS", 
                           "CG", 
                           "SHO", 
                           "SV", 
                           "IPouts", 
                           "H", 
                           "ER", 
                           "HR", 
                           "BB", 
                           "SO",
                           "BAOpp",
                           "ERA",
                           "IBB",
                           "WP",
                           "HBP",
                           "BK",
                           "BFP",
                           "GF",
                           "R",
                           "SH",
                           "SF",
                           "GIDP"
                    FROM "Master"
                    JOIN "Pitching"
	                    ON "Master"."playerID" = "Pitching"."playerID"
                    WHERE 
	                    "Master"."nameFirst" = '%s'
                             AND "Master"."nameLast" = '%s'
                             AND "Master"."playerID" = '%s'
                  """ %(player_first_name, player_last_name, playerID)

    fielding_sql = """
                    SELECT "yearID",
                           "POS", 
                           "G", 
                           "GS", 
                           "InnOuts", 
                           "PO", 
                           "A", 
                           "E", 
                           "DP", 
                           "PB", 
                           "WP", 
                           "SB", 
                           "CS", 
                           "ZR"
                    FROM "Master"
                    JOIN "Fielding"
	                    ON "Master"."playerID" = "Fielding"."playerID"
                    WHERE 
	                    "Master"."nameFirst" = '%s'
                             AND "Master"."nameLast" = '%s'
                             AND "Master"."playerID" = '%s'
                  """ %(player_first_name, player_last_name, playerID)

    outfielding_sql = """
                    SELECT "yearID",
                           "Glf", 
                           "Gcf", 
                           "Grf" 
                    FROM "Master"
                    JOIN "FieldingOF"
	                    ON "Master"."playerID" = "FieldingOF"."playerID"
                    WHERE 
	                    "Master"."nameFirst" = '%s'
                             AND "Master"."nameLast" = '%s'
                             AND "Master"."playerID" = '%s'
                  """ %(player_first_name, player_last_name, playerID)
    
    hitting_career = pd.read_sql_query(batting_sql, engine)
    pitching_career = pd.read_sql_query(pitching_sql, engine)
    fielding_career = pd.read_sql_query(fielding_sql, engine)
    outfielding_career = pd.read_sql_query(outfielding_sql, engine)
    
    
    hitting_table = Table(hitting_career.columns.values.tolist(), hitting_career.values)
    pitching_table = Table(pitching_career.columns.values.tolist(), pitching_career.values)
    fielding_table = Table(fielding_career.columns.values.tolist(), fielding_career.values)
    outfielding_table = Table(outfielding_career.columns.values.tolist(), outfielding_career.values)

    widget_list = []
    hitting_table = Table(hitting_career.columns.values.tolist(), hitting_career.values)
    pitching_table = Table(pitching_career.columns.values.tolist(), pitching_career.values)
    fielding_table = Table(fielding_career.columns.values.tolist(), fielding_career.values)
    outfielding_table = Table(outfielding_career.columns.values.tolist(), outfielding_career.values)
    widget_list.append(hitting_table)
    widget_list.append(pitching_table)
    widget_list.append(fielding_table)
    widget_list.append(outfielding_table)
    return template('view/player_page', widgets=widget_list)

     

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
class Card(object):
    def __init__(self, text, title, type):
        self.name       = 'card'
        self.text       = text

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
        

run(app,debug=True,host='0.0.0.0',port='8080',server="cherrypy")




