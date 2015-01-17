import os
import sys
import csv
from optparse import OptionParser
from datetime import datetime
import psycopg2
import pandas as pd
import numpy as np
from sqlalchemy import create_engine

engine = create_engine("postgresql://postgres:Portage2@localhost/mlb")

def main():
    opts, args = parseOptions()
    print(opts, args)
    if opts.initialize == True:
        initialize()
    elif opts.opt_table != False:
        getSQLTable(opts.opt_table)


def parseOptions():
    parser = OptionParser()
    parser.add_option("-i", "--initialize", help="Initialize and Load Baseball Data", action="store_true",
                      dest="initialize", default=False)
    parser.add_option("-t", "--table", help="Return a table from the database as a pandas DataFrame", 
                      action="store", dest="opt_table", default=False)
    (opts, args) = parser.parse_args()
    return opts, args


def initialize():
    start_time = datetime.now()
    csv_file_list = getCSVFiles()
    parseCSV(csv_file_list)
    end_time = datetime.now()
    initialization_time = (end_time - start_time).strftime("%H:%M:%S")
    print("Start Time: %s" % start_time)
    print("End Time: %s" % end_time)
    print("Elapsed Time: %s" % initialization_time)


def getCSVFiles():
    csv_file_list = []
    for dirs, subdirs, files, in os.walk("res\\"):
       for file in files:
           if file.split(".")[1] == 'csv':
               csv_file_path = os.path.join(dirs, file)
               if csv_file_path not in csv_file_list:
                   csv_file_list.append(csv_file_path)
    return csv_file_list


def parseCSV(csv_file_list):
    for csv_file_path in csv_file_list:
        table_name = str(csv_file_path.split("\\")[1]).replace('.csv', '')
        csv_file = pd.DataFrame.from_csv(csv_file_path)
        print("Importing CSV to table: ",table_name)
        csv_file.to_sql(table_name, engine,'postgresql',if_exists='replace')
        

def getSQLTable(table):
    df_table = pd.read_sql_table(table,engine)
    print(df_table)
    return df_table

    

        
        
        
        



if __name__ == "__main__":
    main()