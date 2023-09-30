import psycopg2
from config import host, user, password, db_name

connection = psycopg2.connect(
        host=host,
        user=user,
        password=password,
        database=db_name
    )

current = connection.cursor()
# добавляем значения в таблицу 
id = 1
name = 'someone'
number = '87777878778'

sql = '''
    INSERT INTO phonebook VALUES (%s, %s, %s); 
'''

current.execute(sql, (id, name, number))

current.close()
connection.commit()
connection.close()