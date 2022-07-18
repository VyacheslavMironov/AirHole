# Документация: https://www.psycopg.org/docs/install.html#quick-install
from psycopg2 import connect


global conn
global cur

# Соединение с базой
conn = connect(dbname="", user="postgres", password="root")

# Взаимодействие с базой происходят через метод курсора execute
cur = conn.cursor()


def newUser(name, surname, email, password):
    cur.execute("""

    """)
    return conn.commit()


def userShow(email, password):
    cur.execute("""

    """)
    return conn.fetchall()



def searchCity(cityName):
    cur.execute("""

    """)
    return conn.fetchall()


def addOrder(**kwargs):
    cur.execute("""

    """)
    return conn.commit()