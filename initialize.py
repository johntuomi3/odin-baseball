from utility import *

def main():
    print("This script will initialize the database and setup a user account for Odin")
    postgres_superuser = input("Enter the username of the postgres superuser: ")
    postgres_password = input("Enter the password of the postgres superuser: ")
    createSuperUser(postgres_superuser, postgres_password)
    createDatabase()
    initialize()

if __name__ == "__main__":
    main()



