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
    INSERT INTO phonebook
    VALUES (%s, %s, %s);
'''
# вставляем данные в телефонную книгу вводя их с консоли

print("ID:")
id = int(input())
print("Name:")
username = input()
print("Phone number:")
number = input()
current.execute(sql, (id, username, number))

current.close()
connection.commit()
connection.close()