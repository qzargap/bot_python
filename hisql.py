import sqlite3
import random


db = sqlite3.connect('hi.db', check_same_thread=False)
sql = db.cursor()

sql.execute("""CREATE TABLE IF NOT EXISTS users(
   id INT PRIMARY KEY,
   hi TEXT
)""")

user = ['Здравствуйте', 'Привет', 'Пламенный привет', 'Хай, хелло', 'Приветствую Вас', 'Приветик ',
        '(Очень) рад вас видеть', 'Приятно вас видеть', 'Всем добра', 'Сердечно приветствую вас',
        '(Очень) рад встрече с вами', 'Приветствую', 'привет', 'hi', 'Hi', 'привет ><']
z = ['hi!']

sqlite_select_query = """SELECT * from users"""
sql.execute(sqlite_select_query)
records = sql.fetchall()


def hi_sql_all(n):
    q = 0
    for i in range(len(n)):
        q += 1
        sql.execute("INSERT INTO users VALUES(?, ?)", (records[-1][0]+q, n[i]))
        db.commit()


def hi_sql(n, q=0):
    q += 1
    sql.execute("INSERT INTO users VALUES(?, ?)", (records[-1][0]+q, n))
    db.commit()


def hi(n):
    str_def(n)
    if n[0] == "/":
        n = n[1:]
    hi_sql(n)


def random_hi():
    return records[random.randint(0, records[-1][0])][1]


def records_all():
    return [records[x][1] for x in range(len(records))]


class str_class:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name

    def __str__(self):
        return str(self.name)


def str_def(n):
    return str_class(n)


