import os
from datetime import datetime
import psycopg2
import pandas as pd
import numpy as np
from sqlalchemy import create_engine


engine = create_engine("postgresql://odin:admin@localhost/odin_app")
start_time = datetime.now()


def initialize():
    print("""******** LOCATING LAHMAN CSV Files ********""")
    csv_file_list = getCSVFiles()
    print("""******** EXTRACTING AND IMPORTING DATA FROM LAHMAN CSV Files ********""")
    parseCSV(csv_file_list)
    end_time = datetime.now()
    initialization_time = end_time - start_time
    print("Start Time: %s" % start_time)
    print("End Time: %s" % end_time)
    print("Elapsed Time: %s" % initialization_time)


def createSuperUser(postgres_superuser, postgres_password):
    print("******** DATABASE USER CREATION ********")
    print("Postgres Superuser: %s \nPostgres Password: %s" %(postgres_superuser, postgres_password))

    try:
        cnxn = psycopg2.connect(user="%s" % (postgres_superuser), password="%s" % (postgres_password))
    except psycopg2.OperationalError:
        print("Invalid Postgres Username or Password")
        exit()
    cur = cnxn.cursor()  
    cur.execute("""do
                    $body$
                    BEGIN
                       IF NOT EXISTS (
                          SELECT *
                          FROM   pg_catalog.pg_user
                          WHERE  usename = 'odin') THEN

                          CREATE ROLE odin WITH SUPERUSER CREATEDB CREATEROLE LOGIN ENCRYPTED PASSWORD 'admin';
                       END IF;
                    END
                $body$;
                """)
    cnxn.commit()
    cur.execute("ALTER USER odin WITH PASSWORD 'admin';")
    cnxn.commit()
    cur.execute("ALTER ROLE odin CREATEDB CREATEROLE REPLICATION;")
    cnxn.commit()  
    cnxn.close()


def createDatabase():
    print("******** DATABASE CREATION ********")
    cnxn2 = psycopg2.connect(database='postgres',user="odin",host="localhost",password="admin")
    cnxn2.autocommit = True
    cur2 = cnxn2.cursor()  
    odin_existance = cur2.execute("""
                                    SELECT datname
                                    FROM   pg_catalog.pg_database
                                    WHERE  datname = 'odin_app'                    
                                  """)    
    if odin_existance == "None":
        cur2.execute("""
                     CREATE DATABASE odin_app OWNER odin TEMPLATE template0;                          
                     """)   
        print("Odin Database Created Successfully") 
    else:
        print("Odin Database Already Exists")
    cnxn2.close()


def getCSVFiles():
    csv_file_list = []
    for dirs, subdirs, files, in os.walk("res\\"):
       for file in files:
           if file.split(".")[1] == 'csv':
               csv_file_path = os.path.join(dirs, file)
               if csv_file_path not in csv_file_list:
                   csv_file_list.append(csv_file_path)
    print("Found %s CSV Files." % (len(csv_file_list)))
    return csv_file_list


def parseCSV(csv_file_list):
    for csv_file_path in csv_file_list:
        table_name = str(csv_file_path.split("\\")[1]).replace('.csv', '')
        csv_file = pd.DataFrame.from_csv(csv_file_path)
        print("Importing CSV to table: ",table_name)
        csv_file.to_sql(table_name, engine,'postgresql',if_exists='replace')
        

def getSQLTable(table):
    df_table = pd.read_sql_table(table,engine)
    return df_table
