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


def update():
    sql.execute(sqlite_select_query)
    rec = sql.fetchall()
    return rec


def user_sql(log, pas, id_users):   # СОЗДАНИЕ НОВОГО ПОЛЬЗОВАТЕЛЯ
    sql.execute("INSERT INTO users VALUES(?, ?, ?, ?, ?)", (update()[-1][0]+1, log, pas, 1, id_users))
    db.commit()


def examination(log, pas, id_users):    # ПРОВЕРКА ЛОГИНА НА УНИКАЛЬНОСТЬ
    if log[0] == '/' or pas[0] == '/':
        return '/'
    if log in [update()[x][1] for x in range(len(update()))]:
        return "Такой логин уже существует"
    user_sql(log, pas, id_users)


def money(login):   # ФАРМ ДЕНЕГ
    for i in range(len(update())):
        if login == update()[i][1]:
            ann(update()[i][3] + 1, update()[i][0], i)


def id_user(log):   # БАЛАНС ПОЛЬЗОВАТЕЛЯ
    for i in range(len(update())):
        if log == update()[i][1]:
            return update()[i][3]


def ann(mone, id_login, i):
    print(update()[i][3], mone)
    sql_update_query = f"""Update users set money = {update()[i][3]+1} where id = {id_login}"""
    sql.execute(sql_update_query)
    db.commit()


def come_users(login, password):    # ПОЛЬЗОВАТЕЛЬ ВХОДИТ
    for i in range(len(update())):
        if login == update()[i][1] and password == update()[i][2]:
            return f"{update()[i][1]} Вы успешно вошли"
    return "Неправильный логин или пароль"


if __name__ == "__main__":
    if 'oleg' in [update()[x][1] for x in range(len(update()))]:
        print("Существует")
