import psycopg2
from config import host, user, password, db_name

connection = psycopg2.connect(
        host=host,
        user=user,
        password=password,
        database=db_name
    )

current = connection.cursor()
del_data = input("By what do you want to delete?: ")
del_data = del_data.lower()
temp = input(f'Which {del_data} do you want to delete?: ')
if del_data == 'name':
    sql = '''
        DELETE FROM phonebook WHERE name = %s RETURNING *
    '''
elif del_data == 'number':
    sql = '''
        DELETE FROM phonebook WHERE number = %s RETURNING *
    '''
current.execute(sql, (temp,))
connection.commit()
current.close()
connection.close()