import os
import sys
import csv
import psycopg2
import pandas as pd
import numpy as np
from pandas.io import sql
import psycopg2


conn = psycopg2.connect(database="mlb")

def main():
    initialize()


def initialize():
    csv_file_list = getCSVFiles()
    parseCSV(csv_file_list)


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
        print(table_name)
        csv_file = pd.read_csv(csv_file_path)
        

        
        
        
        



if __name__ == "__main__":
    main()