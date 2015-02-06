from bottle import Bottle, route, run, template, static_file
from utility import *
from database import *
app = Bottle()

 
#TODO: Trim Team Roster Queries
#TODO: Format Player Page better
#TODO: Start Experimenting with Projections ex. Trend Last 3 Years League Average WAR vs Player WAR
#TODO: Change Last 3 Years to be a provided value ex. Last 10 years
#TODO: Implement Team Specific Views
#TODO: Add Salary Specific Views
#TODO: Add Player Search Functionality
#TODO: Work on Nav Bar

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
    if len(str(player_name).split(' ')) == 3:
        player_first_name = str(player_name.split(' ')[0] + ' ' + player_name.split(' ')[1]).title()
        player_last_name = str(player_name.split(' ')[2]).title()
    else:
        if len(str(player_name.split(' ')[0])) == 2:
            player_first_name = str(player_name.split(' ')[0]).upper()
        else:
            player_first_name = str(player_name.split(' ')[0]).title()
            player_last_name = str(player_name.split(' ')[1]).title()
    print(player_first_name, player_last_name)
    
    
    player_selection = pd.read_sql_query(sqlPlayerSearchResults(player_first_name,player_last_name), engine)
    hitting_career = pd.read_sql_query(sqlBattingCareer(player_first_name, player_last_name), engine)
    pitching_career = pd.read_sql_query(sqlPitchingCareer(player_first_name, player_last_name), engine)
    fielding_career = pd.read_sql_query(sqlFieldingCareer(player_first_name, player_last_name), engine)


    player_choice = player_selection.drop_duplicates()
    print(player_choice)
    if len(player_choice) > 1:
        html_string = "<ul>"
        for i in player_choice.values.tolist():
            html_string +=("<li><a href=\"/player/"+ player_name +"/" + i[0]+ "/" + i[1] + "\">" + i[1]  + " " + str(player_name).title() + "</a></li>")
        html_string += "</ul>"
        print(html_string)
        panel = Panel(html_string,'Multiple Players Found','warning')
        return template('view/default_container', widget=panel.name, panel_type=panel.type, text=panel.text, title=panel.title)
        
    else:
        widget_list = []
        hitting_table = Table("Batting Career",hitting_career.columns.values.tolist(), hitting_career.values)
        pitching_table = Table("Pitching Career",pitching_career.columns.values.tolist(), pitching_career.values)
        fielding_table = Table("Fielding Career",fielding_career.columns.values.tolist(), fielding_career.values)
        no_data_card = Card(text = "<center><h1>No Data</h1></center>")

        widget_list = []
        if len(hitting_career.values) != 0:
            widget_list.append(hitting_table)
        else:
            no_data_card.text = "<center><h1>No Batting Data Available</h1></center>"
            widget_list.append(no_data_card)
        if len(pitching_career.values) != 0:
            widget_list.append(pitching_table)
        else:
            no_data_card.text = "<center><h1>No Pitching Data Available</h1></center>"        
            widget_list.append(no_data_card)
        if len(fielding_career.values) != 0:    
            widget_list.append(fielding_table)
        else:
            no_data_card.text = "<center><h1>No Fielding Data Available</h1></center>"
            widget_list.append(no_data_card)
        return template('view/player_page', widgets=widget_list)


@app.route('/player/<player_name>/<playerID>')
@app.route('/player/<player_name>/<playerID>/')
def player(player_name, playerID):
    if len(str(player_name).split(' ')) == 3:
        player_first_name = str(player_name.split(' ')[0] + ' ' + player_name.split(' ')[1]).title()
        player_last_name = str(player_name.split(' ')[2]).title()
    else:
        if len(str(player_name.split(' ')[0])) == 2:
            player_first_name = str(player_name.split(' ')[0]).upper()
        else:
            player_first_name = str(player_name.split(' ')[0]).title()
        player_last_name = str(player_name.split(' ')[1]).title()
   
            
    hitting_career = pd.read_sql_query(sqlBattingCareer(player_first_name, player_last_name,playerID), engine)
    pitching_career = pd.read_sql_query(sqlPitchingCareer(player_first_name, player_last_name,playerID), engine)
    fielding_career = pd.read_sql_query(sqlFieldingCareer(player_first_name, player_last_name,playerID), engine)
    
        
    hitting_table = Table("Batting Career",hitting_career.columns.values.tolist(), hitting_career.values)
    pitching_table = Table("Pitching Career",pitching_career.columns.values.tolist(), pitching_career.values)
    fielding_table = Table("Fielding Career",fielding_career.columns.values.tolist(), fielding_career.values)
    no_data_card = Card("<center><h1>No Data</h1></center>")

    widget_list = []
    if len(hitting_career.values) != 0:
        widget_list.append(hitting_table)
    else:
        no_data_card.text = "<center><h1>No Batting Data Available</h1></center>"
        widget_list.append(no_data_card)
    if len(pitching_career.values) != 0:
        widget_list.append(pitching_table)
    else:
        no_data_card.text = "<center><h1>No Pitching Data Available</h1></center>"        
        widget_list.append(no_data_card)
    if len(fielding_career.values) != 0:    
        widget_list.append(fielding_table)
    else:
        no_data_card.text = "<center><h1>No Fielding Data Available</h1></center>"
        widget_list.append(no_data_card)
    return template('view/player_page', widgets=widget_list)
    


@app.route('/player/<player_name>/<playerID>/career')
@app.route('/player/<player_name>/<playerID>/career/')
def playerCareer(player_name, playerID):
    if len(str(player_name).split(' ')) == 3:
        player_first_name = str(player_name.split(' ')[0] + ' ' + player_name.split(' ')[1]).title()
        player_last_name = str(player_name.split(' ')[2]).title()
    else:
        if len(str(player_name.split(' ')[0])) == 2:
            player_first_name = str(player_name.split(' ')[0]).upper()
        else:
            player_first_name = str(player_name.split(' ')[0]).title()
        player_last_name = str(player_name.split(' ')[1]).title()
    
    
    hitting_career = pd.read_sql_query(sqlBattingCareer(player_first_name, player_last_name,playerID), engine)
    pitching_career = pd.read_sql_query(sqlPitchingCareer(player_first_name, player_last_name,playerID), engine)
    fielding_career = pd.read_sql_query(sqlFieldingCareer(player_first_name, player_last_name,playerID), engine)
    
    
    hitting_table = Table("Batting Career",hitting_career.columns.values.tolist(), hitting_career.values)
    pitching_table = Table("Pitching Career",pitching_career.columns.values.tolist(), pitching_career.values)
    fielding_table = Table("Fielding Career",fielding_career.columns.values.tolist(), fielding_career.values)
    no_data_card = Card("<center><h1>No Data</h1></center>")

    widget_list = []
    if len(hitting_career.values) != 0:
        widget_list.append(hitting_table)
    else:
        no_data_card.text = "<center><h1>No Batting Data Available</h1></center>"
        widget_list.append(no_data_card)
    if len(pitching_career.values) != 0:
        widget_list.append(pitching_table)
    else:
        no_data_card.text = "<center><h1>No Pitching Data Available</h1></center>"        
        widget_list.append(no_data_card)
    if len(fielding_career.values) != 0:    
        widget_list.append(fielding_table)
    else:
        no_data_card.text = "<center><h1>No Fielding Data Available</h1></center>"
        widget_list.append(no_data_card)
    return template('view/player_page', widgets=widget_list)



@app.route('/player/<player_name>/<playerID>/<teamID>')
@app.route('/player/<player_name>/<playerID>/<teamID>/')
def playerTeamCareer(player_name, playerID, teamID):
    if len(str(player_name).split(' ')) == 3:
        player_first_name = str(player_name.split(' ')[0] + ' ' + player_name.split(' ')[1]).title()
        player_last_name = str(player_name.split(' ')[2]).title()
    else:
        if len(str(player_name.split(' ')[0])) == 2:
            player_first_name = str(player_name.split(' ')[0]).upper()
        else:
            player_first_name = str(player_name.split(' ')[0]).title()
        player_last_name = str(player_name.split(' ')[1]).title()
    
    
    hitting_career = pd.read_sql_query(sqlBattingCareer(player_first_name, player_last_name,playerID,teamID), engine)
    pitching_career = pd.read_sql_query(sqlPitchingCareer(player_first_name, player_last_name,playerID,teamID), engine)
    fielding_career = pd.read_sql_query(sqlFieldingCareer(player_first_name, player_last_name,playerID,teamID), engine)
    
    
    hitting_table = Table("Batting Career",hitting_career.columns.values.tolist(), hitting_career.values)
    pitching_table = Table("Pitching Career",pitching_career.columns.values.tolist(), pitching_career.values)
    fielding_table = Table("Fielding Career",fielding_career.columns.values.tolist(), fielding_career.values)
    no_data_card = Card("<center><h1>No Data</h1></center>")

    widget_list = []
    if len(hitting_career.values) != 0:
        widget_list.append(hitting_table)
    else:
        no_data_card.text = "<center><h1>No Batting Data Available</h1></center>"
        widget_list.append(no_data_card)
    if len(pitching_career.values) != 0:
        widget_list.append(pitching_table)
    else:
        no_data_card.text = "<center><h1>No Pitching Data Available</h1></center>"        
        widget_list.append(no_data_card)
    if len(fielding_career.values) != 0:    
        widget_list.append(fielding_table)
    else:
        no_data_card.text = "<center><h1>No Fielding Data Available</h1></center>"
        widget_list.append(no_data_card)
    return template('view/player_page', widgets=widget_list)


@app.route('/reportcard/<player_name>/<playerID>/<teamID>')
@app.route('/reportcard/<player_name>/<playerID>/<teamID>/')
def reportCard(player_name, playerID, teamID):
    if len(str(player_name).split(' ')) == 3:
        player_first_name = str(player_name.split(' ')[0] + ' ' + player_name.split(' ')[1]).title()
        player_last_name = str(player_name.split(' ')[2]).title()
    else:
        if len(str(player_name.split(' ')[0])) == 2:
            player_first_name = str(player_name.split(' ')[0]).upper()
        else:
            player_first_name = str(player_name.split(' ')[0]).title()
        player_last_name = str(player_name.split(' ')[1]).title()
    
    
    hitting_avg3 = pd.read_sql_query(sqlBattingCareerLastThree(player_first_name, player_last_name,playerID,teamID), engine)
    pitching_avg3 = pd.read_sql_query(sqlPitchingCareerLastThreeYears(player_first_name, player_last_name,playerID,teamID), engine)
    #fielding_career = pd.read_sql_query(sqlFieldingCareer(player_first_name, player_last_name,playerID,teamID), engine)

    mlb_hitting = pd.read_sql_query(sqlMLBAverageBattingLastThreeYears(),engine)
    mlb_pitching = pd.read_sql_query(sqlMLBAveragePitchingLastThreeYears(),engine)
    
    
    hitting_table = Table("Batting Averages over 3 Years",hitting_avg3.columns.values.tolist(), hitting_avg3.values)
    pitching_table = Table("Pitching Averages over 3 Years",pitching_avg3.columns.values.tolist(), pitching_avg3.values)
    #fielding_table = Table("Fielding Career",fielding_career.columns.values.tolist(), fielding_career.values)
    mlb_hitting_table = Table("MLB Average Hitting over 3 Years", mlb_hitting.columns.tolist(), mlb_hitting.values)
    mlb_pitching_table = Table("MLB Average Pitching over 3 Years", mlb_pitching.columns.tolist(), mlb_pitching.values)

    no_data_card = Card("<center><h1>No Data</h1></center>")

    widget_list = []
    if len(hitting_avg3.values) != 0:
        widget_list.append(hitting_table)
        widget_list.append(mlb_hitting_table)
    else:
        no_data_card.text = "<center><h1>No Batting Data Available</h1></center>"
        widget_list.append(no_data_card)
    if len(pitching_avg3.values) != 0:
        widget_list.append(pitching_table)
        widget_list.append(mlb_pitching_table)
    else:
        no_data_card.text = "<center><h1>No Pitching Data Available</h1></center>"        
        widget_list.append(no_data_card)
    #if len(fielding_career.values) != 0:    
    #    widget_list.append(fielding_table)
    #else:
    #    no_data_card.text = "<center><h1>No Fielding Data Available</h1></center>"
    #    widget_list.append(no_data_card)
    
    
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
    def __init__(self, text):
        self.name       = 'card'
        self.text       = text


class Panel(object):
    def __init__(self, text, title, type):
        self.name       = 'panel'
        self.text       = text
        self.title      = title        
        self.type       = type
        

class Table(object):
    def __init__(self, title, fields, data):
        self.name       = 'table'
        self.title      = title  
        self.fields     = fields
        self.data       = data
        
run(app,debug=True,host='0.0.0.0',port='8080',server="cherrypy")
