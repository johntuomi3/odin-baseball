import os
import sys
from utility import *

def main():
    #modules = []
    #with open('res/requirements.txt','r') as f:
    #    for line in f:
    #        modules.append(line.replace('\n',''))
    #print("Odin requires the following packages to be installed before use: \n")
    #print(modules)
                
    #install_dependent_packages = input("\nInstall the required packages? (Y or N): ")
    #if install_dependent_packages == 'Y':
    #    os.system("""pip install -r res/requirements.txt""")
    #elif install_dependent_packages == 'N':
    #    print("Odin cannot function without the packages listed in res/requirements.txt")
    #    print("Exiting...")
    #    exit()
    #else:
    #    print("Invalid option: ", install_dependent_packages)
    #    print("Odin cannot function without the packages listed in res/requirements.txt")
    #    print("Exiting...")
    #    exit()
    #print("\nThis script will initialize the database and setup a user account for Odin")
    #postgres_superuser = input("\nEnter the username of the postgres superuser: ")
    #postgres_password = input("Enter the password of the postgres superuser: ")
    #createSuperUser(postgres_superuser, postgres_password)
    #createDatabase()
    #initialize()
    fixTeamTable()

if __name__ == "__main__":
    main()



