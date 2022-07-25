# Документация: https://www.psycopg.org/docs/install.html#quick-install
from psycopg2 import connect


global conn
global cur

# Соединение с базой
conn = connect(dbname="airhole", user="postgres", password="root")

# Взаимодействие с базой происходят через метод курсора execute
cur = conn.cursor()


def newUser(name, surname, email, password):
    query = "INSERT INTO users('name', 'surname', 'email', 'password')"
    query += 'VALUES("{name}", "{surname}", "{email}", "{password}");'
    cur.execute(query)
    return conn.commit()


def userShow(email, password):
    lists=[]
    cur.execute(f"SELECT * FROM users WHERE email='{email}' AND password='{password}';")
    row = conn.fetchall()
    
    for i in row:
        lists.append(i)

    if len(lists) > 0:
        return lists



def searchCity(cityName):
    cur.execute(f"SELECT * FROM aircraft WHERE city_out={cityName};")
    return conn.fetchall()


def addOrder(user_id, order_id. aircraft_id):
    query = "INSERT INTO orders('user_id', 'order_id', 'aircraft_id')"
    query += f'VALUES({user_id}, {order_id}, {aircraft_id});'
    cur.execute(query)
    return conn.commit()