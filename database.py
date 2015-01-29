def sqlPlayerSearchResults(player_first_name, player_last_name, playerID=None):
    if playerID == None:
        sql = """
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
    elif playerID != None:
        sql = """
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
                                 AND "Master"."playerID" = '%s'
                     """ %(player_first_name, player_last_name, playerID)

    return sql


def sqlBattingCareer(player_first_name, player_last_name, playerID=None, teamID=None):
    if playerID == None:
        sql = """
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

    elif playerID != None and teamID == None:
        sql = """
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

    elif playerID != None and teamID != None:
        sql = """
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
                                 AND "Batting"."teamID" = '%s'
             """ %(player_first_name, player_last_name, playerID, teamID)
    return sql


def sqlPitchingCareer(player_first_name, player_last_name, playerID=None, teamID=None):
    if playerID == None:
        sql = """
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
    elif playerID != None and teamID == None:
                sql = """
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
    elif playerID != None and teamID != None:
                sql = """
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
                                 AND "Pitching"."teamID" = '%s'
                      """ %(player_first_name, player_last_name, playerID, teamID)
    return sql


def sqlFieldingCareer(player_first_name, player_last_name, playerID=None, teamID=None):
    if playerID == None:
        sql = """
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
    if playerID != None and teamID == None:
        sql = """
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

    if playerID != None and teamID != None:
        sql = """
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
                             AND "Fielding"."teamID" = '%s'
            """ %(player_first_name, player_last_name, teamID)
    return sql
