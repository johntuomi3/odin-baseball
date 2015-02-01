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


def sqlBattingCareerLastThree(player_first_name, player_last_name, playerID=None, teamID=None):
    if playerID == None:
        sql = """
                        
			SELECT SUM(p."G")/3.000		G_3AVG
			      ,SUM(p."AB")/3.000	AB_3AVG
			      ,SUM(p."R")/3.000		R_3AVG
			      ,SUM(p."H")/3.000		H_3AVG
			      ,SUM(p."2B")/3.000	"2B_3AVG"
			      ,SUM(p."3B")/3.000	"3B_3AVG"
			      ,SUM(p."HR")/3.000	HR_3AVG
			      ,SUM(p."RBI")/3.000	RBI_3AVG
			      ,SUM(p."SB")/3.000	SB_3AVG
			      ,SUM(p."CS")/3.000	CS_3AVG
			      ,SUM(p."BB")/3.000	BB_3AVG
			      ,SUM(p."SO")/3.000	SO_3AVG
			      ,SUM(p."IBB")/3.000	IBB_3AVG
			      ,SUM(p."HBP")/3.000	HBP_3AVG
			      ,SUM(p."SH")/3.000	SH_3AVG
			      ,SUM(p."SF")/3.000	SF_3AVG
			      ,SUM(p."GIDP")/3.000	GIDP_3AVG
			FROM(
				    SELECT "Batting"."yearID"   "yearID", 
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
				    ORDER BY
					    "Batting"."yearID" DESC
				    LIMIT 3
                        ) AS p
             """ %(player_first_name, player_last_name)

    elif playerID != None and teamID == None:
        sql = """
                        
			SELECT SUM(p."G")/3.000		G_3AVG
			      ,SUM(p."AB")/3.000	AB_3AVG
			      ,SUM(p."R")/3.000		R_3AVG
			      ,SUM(p."H")/3.000		H_3AVG
			      ,SUM(p."2B")/3.000	"2B_3AVG"
			      ,SUM(p."3B")/3.000	"3B_3AVG"
			      ,SUM(p."HR")/3.000	HR_3AVG
			      ,SUM(p."RBI")/3.000	RBI_3AVG
			      ,SUM(p."SB")/3.000	SB_3AVG
			      ,SUM(p."CS")/3.000	CS_3AVG
			      ,SUM(p."BB")/3.000	BB_3AVG
			      ,SUM(p."SO")/3.000	SO_3AVG
			      ,SUM(p."IBB")/3.000	IBB_3AVG
			      ,SUM(p."HBP")/3.000	HBP_3AVG
			      ,SUM(p."SH")/3.000	SH_3AVG
			      ,SUM(p."SF")/3.000	SF_3AVG
			      ,SUM(p."GIDP")/3.000	GIDP_3AVG
			FROM(
				SELECT "Batting"."yearID"   "yearID", 
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
				ORDER BY
					"Batting"."yearID" DESC
				LIMIT 3
                        ) AS p

             """ %(player_first_name, player_last_name, playerID)

    elif playerID != None and teamID != None:
        sql = """
                        
			SELECT SUM(p."G")/3.000		G_3AVG
			      ,SUM(p."AB")/3.000	AB_3AVG
			      ,SUM(p."R")/3.000		R_3AVG
			      ,SUM(p."H")/3.000		H_3AVG
			      ,SUM(p."2B")/3.000	"2B_3AVG"
			      ,SUM(p."3B")/3.000	"3B_3AVG"
			      ,SUM(p."HR")/3.000	HR_3AVG
			      ,SUM(p."RBI")/3.000	RBI_3AVG
			      ,SUM(p."SB")/3.000	SB_3AVG
			      ,SUM(p."CS")/3.000	CS_3AVG
			      ,SUM(p."BB")/3.000	BB_3AVG
			      ,SUM(p."SO")/3.000	SO_3AVG
			      ,SUM(p."IBB")/3.000	IBB_3AVG
			      ,SUM(p."HBP")/3.000	HBP_3AVG
			      ,SUM(p."SH")/3.000	SH_3AVG
			      ,SUM(p."SF")/3.000	SF_3AVG
			      ,SUM(p."GIDP")/3.000	GIDP_3AVG
			FROM(
				SELECT "Batting"."yearID"   "yearID", 
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
				ORDER BY
					"Batting"."yearID" DESC
				LIMIT 3
                        ) AS p
             """ %(player_first_name, player_last_name, playerID, teamID)
    return sql


def sqlMLBAverageBattingLastThreeYears():
    sql = """
            SELECT   SUM("TOTAL_G")    		    MLB_3AVG_G
	                ,SUM("TOTAL_AB")			MLB_3AVG_AB
	                ,SUM("TOTAL_R")				MLB_3AVG_R
	                ,SUM("TOTAL_H")				MLB_3AVG_H
	                ,SUM("TOTAL_2B")			MLB_3AVG_2B
	                ,SUM("TOTAL_3B")			MLB_3AVG_3B
	                ,SUM("TOTAL_HR")			MLB_3AVG_HR
	                ,SUM("TOTAL_RBI")			MLB_3AVG_RBI
	                ,SUM("TOTAL_SB")			MLB_3AVG_SB
	                ,SUM("TOTAL_CS")			MLB_3AVG_CS
	                ,SUM("TOTAL_BB")			MLB_3AVG_BB
	                ,SUM("TOTAL_SO")			MLB_3AVG_SO	
	                ,SUM("TOTAL_IBB")			MLB_3AVG_IBB
	                ,SUM("TOTAL_HBP")			MLB_3AVG_HBP
	                ,SUM("TOTAL_SH")			MLB_3AVG_SH
	                ,SUM("TOTAL_SF")			MLB_3AVG_SF
	                ,SUM("TOTAL_GIDP")		                                                            MLB_3AVG_GIDP
	                ,SUM("TOTAL_H")/SUM("TOTAL_AB")      																	MLB_3AVG_BAT_AVG
	                ,SUM("TOTAL_H") - (SUM("TOTAL_2B") + SUM("TOTAL_3B") + SUM("TOTAL_HR")) 												MLB_3AVG_1B
	                ,(SUM("TOTAL_H") - (SUM("TOTAL_2B") + SUM("TOTAL_3B") + SUM("TOTAL_HR"))) + (SUM("TOTAL_2B") * 2) + (SUM("TOTAL_3B")* 3) + (SUM("TOTAL_HR") * 4) 			MLB_3AVG_TB
	                ,((SUM("TOTAL_H") - (SUM("TOTAL_2B") + SUM("TOTAL_3B") + SUM("TOTAL_HR"))) + (SUM("TOTAL_2B") * 2) + (SUM("TOTAL_3B")* 3) + (SUM("TOTAL_HR") * 4))/SUM("TOTAL_AB")	MLB_3AVG_SLUG
	                ,(SUM("TOTAL_H") + SUM("TOTAL_BB") + SUM("TOTAL_IBB") + SUM("TOTAL_HBP"))/(SUM("TOTAL_AB")+ SUM("TOTAL_BB") + SUM("TOTAL_IBB") + SUM("TOTAL_HBP")+ SUM("TOTAL_SF")) 	MLB_3AVG_OBP
                FROM(
                SELECT	"Batting"."yearID"
	                ,SUM("G")/c.NUM_PLAYERS		"TOTAL_G"
	                ,SUM("AB")/c.NUM_PLAYERS	"TOTAL_AB"
	                ,SUM("R")/c.NUM_PLAYERS		"TOTAL_R"		
	                ,SUM("H")/c.NUM_PLAYERS		"TOTAL_H"
	                ,SUM("2B")/c.NUM_PLAYERS	"TOTAL_2B"
	                ,SUM("3B")/c.NUM_PLAYERS	"TOTAL_3B"
	                ,SUM("HR")/c.NUM_PLAYERS	"TOTAL_HR"
	                ,SUM("RBI")/c.NUM_PLAYERS	"TOTAL_RBI"
	                ,SUM("SB")/c.NUM_PLAYERS	"TOTAL_SB"
	                ,SUM("CS")/c.NUM_PLAYERS	"TOTAL_CS"
	                ,SUM("BB")/c.NUM_PLAYERS	"TOTAL_BB"
	                ,SUM("SO")/c.NUM_PLAYERS	"TOTAL_SO"
	                ,SUM("IBB")/c.NUM_PLAYERS	"TOTAL_IBB"
	                ,SUM("HBP")/c.NUM_PLAYERS	"TOTAL_HBP"
	                ,SUM("SH")/c.NUM_PLAYERS	"TOTAL_SH"
	                ,SUM("SF")/c.NUM_PLAYERS	"TOTAL_SF"
	                ,SUM("GIDP")/c.NUM_PLAYERS	"TOTAL_GIDP"
	                ,c.NUM_PLAYERS
	
                FROM
	                "Batting"
                LEFT JOIN
	                (SELECT 	COUNT(DISTINCT "playerID") NUM_PLAYERS
	                       ,"yearID"
	                 FROM
		                "Batting"

	                 GROUP BY
		                "yearID") as c
                ON "Batting"."yearID" = c."yearID"

		
                GROUP BY
	                "Batting"."yearID"
	                ,c.NUM_PLAYERS
                ORDER BY
                "yearID" DESC

                LIMIT 3
                ) as N
          """
    return sql

def sqlMLBAveragePitchingLastThreeYears():
    sql = """
            SELECT   SUM("TOTAL_W")    		        MLB_3AVG_W
	                ,SUM("TOTAL_L")				MLB_3AVG_L
	                ,SUM("TOTAL_G")				MLB_3AVG_G
	                ,SUM("TOTAL_GS")			MLB_3AVG_GS
	                ,SUM("TOTAL_CG")			MLB_3AVG_CG
	                ,SUM("TOTAL_SHO")			MLB_3AVG_SHO
	                ,SUM("TOTAL_SV")			MLB_3AVG_SV
	                ,SUM("TOTAL_IPOUTS")			MLB_3AVG_IPOUTS
	                ,SUM("TOTAL_H")				MLB_3AVG_H
	                ,SUM("TOTAL_ER")			MLB_3AVG_ER
	                ,SUM("TOTAL_HR")			MLB_3AVG_HR
	                ,SUM("TOTAL_BB")			MLB_3AVG_BB	
	                ,SUM("TOTAL_SO")			MLB_3AVG_SO
	                ,SUM("TOTAL_BAOPP")			MLB_3AVG_BAOPP
	                ,SUM("TOTAL_ERA")				MLB_3AVG_ERA
	                ,SUM("TOTAL_IBB")				MLB_3AVG_IBB
	                ,SUM("TOTAL_WP")		     		MLB_3AVG_WP
	                ,SUM("TOTAL_HBP")		     		MLB_3AVG_HBP
	                ,SUM("TOTAL_BK")		     		MLB_3AVG_BK
	                ,SUM("TOTAL_BFP")		     		MLB_3AVG_BFP
	                ,SUM("TOTAL_GF")		     		MLB_3AVG_GF
	                ,SUM("TOTAL_R")		     			MLB_3AVG_R
	                ,SUM("TOTAL_SH")		     		MLB_3AVG_SH
	                ,SUM("TOTAL_SF")		     		MLB_3AVG_SF
	                ,SUM("TOTAL_GIDP")		     		MLB_3AVG_GIDP
                FROM(
                SELECT	"Pitching"."yearID"
	                ,SUM("W")/c.NUM_PLAYERS		"TOTAL_W"
	                ,SUM("L")/c.NUM_PLAYERS		"TOTAL_L"
	                ,SUM("G")/c.NUM_PLAYERS		"TOTAL_G"		
	                ,SUM("GS")/c.NUM_PLAYERS	"TOTAL_GS"
	                ,SUM("CG")/c.NUM_PLAYERS	"TOTAL_CG"
	                ,SUM("SHO")/c.NUM_PLAYERS	"TOTAL_SHO"
	                ,SUM("SV")/c.NUM_PLAYERS	"TOTAL_SV"
	                ,SUM("IPouts")/c.NUM_PLAYERS	"TOTAL_IPOUTS"
	                ,SUM("H")/c.NUM_PLAYERS		"TOTAL_H"
	                ,SUM("ER")/c.NUM_PLAYERS	"TOTAL_ER"
	                ,SUM("HR")/c.NUM_PLAYERS	"TOTAL_HR"
	                ,SUM("BB")/c.NUM_PLAYERS	"TOTAL_BB"
	                ,SUM("SO")/c.NUM_PLAYERS	"TOTAL_SO"
	                ,SUM("BAOpp")/c.NUM_PLAYERS	"TOTAL_BAOPP"
	                ,SUM("ERA")/c.NUM_PLAYERS	"TOTAL_ERA"
	                ,SUM("IBB")/c.NUM_PLAYERS	"TOTAL_IBB"
	                ,SUM("WP")/c.NUM_PLAYERS	"TOTAL_WP"
	                ,SUM("HBP")/c.NUM_PLAYERS	"TOTAL_HBP"
	                ,SUM("BK")/c.NUM_PLAYERS	"TOTAL_BK"
	                ,SUM("BFP")/c.NUM_PLAYERS	"TOTAL_BFP"
	                ,SUM("GF")/c.NUM_PLAYERS	"TOTAL_GF"
	                ,SUM("R")/c.NUM_PLAYERS		"TOTAL_R"
	                ,SUM("SH")/c.NUM_PLAYERS	"TOTAL_SH"
	                ,SUM("SF")/c.NUM_PLAYERS	"TOTAL_SF"
	                ,SUM("GIDP")/c.NUM_PLAYERS	"TOTAL_GIDP"
	                ,c.NUM_PLAYERS
	
                FROM
	                "Pitching"
                LEFT JOIN
	                (SELECT 	COUNT(DISTINCT "playerID") NUM_PLAYERS
	                       ,"yearID"
	                 FROM
		                "Pitching"

	                 GROUP BY
		                "yearID") as c
                ON "Pitching"."yearID" = c."yearID"

		
                GROUP BY
	                "Pitching"."yearID"
	                ,c.NUM_PLAYERS
                ORDER BY
                "yearID" DESC

                LIMIT 3
                ) as N
          """