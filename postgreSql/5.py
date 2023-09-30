import psycopg2
from config import host, user, password, db_name

connection = psycopg2.connect(
        host=host,
        user=user,
        password=password,
        database=db_name
    )

current = connection.cursor()

# запрос id, name, number по отсортированному имени 
sql1 = '''
    SELECT id, name, number FROM phonebook ORDER BY name ASC
'''
# запрос номера телефона определенного человека 
sql2 = '''
    SELECT number FROM phonebook WHERE name = 'Mama'
'''
current.execute(sql2)

final = current.fetchall()
print(final)
current.close()
connection.commit()
connection.close()