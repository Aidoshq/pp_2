import psycopg2
from config import host, user, password, db_name


try:
    #connect to exist database
    connection = psycopg2.connect(
        host = host
        user = user
        password = password
        database = db_name
    )

    #the cursor for performing database operations
    cursor = connection.cursor()

    with connection.cursor() as cursor:
        pass


except Exception as _ex:
    print("[INFO] Error while working with PostgreSQL" _ex)
finally
    if connection:
        #cursor.close()
        #connection.close()
        print("[INFO] PostgreSqL connection closed")
