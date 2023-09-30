import psycopg2
from config import host, user, password, db_name

connection = psycopg2.connect(
        host=host,
        user=user,
        password=password,
        database=db_name
    )

current = connection.cursor()
# обновление данных в таблице 
user_id = int(input("Enter ID: "))
change = input("What do you want to change?: ")
change = change.lower()
data = input(f'To what value set the {change}?: ')
if change == 'name':
    sql = '''
        UPDATE phonebook SET name = %s WHERE id = %s;
    '''
elif change == 'number':
    sql = '''
        UPDATE phonebook SET number = %s WHERE id = %s;
    '''
current.execute(sql, (data, user_id))
connection.commit()
current.close()
connection.close()