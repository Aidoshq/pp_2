import psycopg2
from config import host, user, password, db_name

connection = psycopg2.connect(
        host=host,
        user=user,
        password=password,
        database=db_name
    )

current = connection.cursor()
sql = '''
        CREATE TABLE phonebook(
            id INTEGER PRIMARY KEY,
            name VARCHAR(100),
            number VARCHAR(12)
    );
'''
current.execute(sql)

current.close()
connection.commit()
connection.close()