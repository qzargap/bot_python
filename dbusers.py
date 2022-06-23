import random
import sqlite3
db = sqlite3.connect('users.db', timeout=10, check_same_thread=False)
sql = db.cursor()

sql.execute("""CREATE TABLE IF NOT EXISTS users(
   id INT PRIMARY KEY,
   login TEXT,
   password TEXT
)""")

sqlite_select_query = """SELECT * from users"""
sql.execute(sqlite_select_query)
us_log = sql.fetchall()
author = 'id_users'
# sql.execute("alter table users add column '%s' 'INTEGER'" % author)
db.commit()


def update():   # ОБНОВЛЕНИЕ БАЗЫ ДАННЫХ
    return sql.execute(sqlite_select_query).fetchall()


def money(login):   # ФАРМ ДЕНЕГ
    a = int(str([x for x in range(len(update())) if login == update()[x][1]])[1:2])
    sql.execute(f"""Update users set money = {update()[a][3] + 1} where id = {update()[a][0]}""")
    db.commit()


def id_user(log):   # БАЛАНС ПОЛЬЗОВАТЕЛЯ
    a = int(str([x for x in range(len(update()))if log == update()[x][1]])[1:2])
    return update()[a][3]


def come_users(login, password):    # ПОЛЬЗОВАТЕЛЬ ВХОДИТ
    try:
        a = int(str([x for x in range(len(update())) if login == update()[x][1] and password == update()[x][2]])[1:2])
        return f"{update()[a][1]} Вы успешно вошли"
    except:
        return "Неправильный логин или пароль"


def examination(log, pas, id_users):    # СОЗДАНИЕ НОВОГО ПОЛЬЗОВАТЕЛЯ
    if log[0] == '/' or pas[0] == '/':
        return '/'
    elif log in [update()[x][1] for x in range(len(update()))]:
        return "Такой логин уже существует"
    sql.execute("INSERT INTO users VALUES(?, ?, ?, ?, ?)", (update()[-1][0] + 1, log, pas, 1, id_users))
    db.commit()


if __name__ == "__main__":
    pass
