import sqlite3
from random import shuffle

from app import app
from flask import g


def add_question(test, question, ans1, ans2, correct):
    connection = sqlite3.connect('app/app.db', check_same_thread=False)
    cursor = connection.cursor()
    msg = ''
    try:
        cursor.execute(f"""INSERT INTO {test}
                        (question, ans1, ans2, correct) VALUES
                        {(question, ans1, ans2, correct)}""")
        connection.commit()
        msg = "SUCCESS"
    except Exception as er:
        connection.rollback()
        msg = f'{er}'
    finally:
        connection.close()
        return msg


def get_all_tests(table_name):
    connection = sqlite3.connect('app/app.db', check_same_thread=False)
    cursor = connection.cursor()
    cursor.execute(f'SELECT * from {table_name}')
    all_tests = cursor.fetchall()
    mixed_tests = {}
    for test in all_tests:
        l = list({test[1]: False, test[2]: False, test[3]: True}.items())
        shuffle(l)
        d_shuffled = dict(l)
        mixed_tests[test[0]] = d_shuffled

        print(d_shuffled)
    print(mixed_tests)
    return mixed_tests


def create_new_table(name):
    connection = sqlite3.connect('app/app.db', check_same_thread=False)
    cursor = connection.cursor()
    try:
        cursor.execute(f'CREATE TABLE {name} (question TEXT, ans1 TEXT, ans2 TEXT, correct TEXT)')
        msg = 'SUCCESS'
    except Exception as er:
        msg = str(er)
    return msg


def delete_new_table(name):
    connection = sqlite3.connect('app/app.db', check_same_thread=False)
    cursor = connection.cursor()
    try:
        cursor.execute(f'DROP TABLE {name}')
        msg = 'SUCCESS'
    except:
        msg = 'ERROR'
    return msg


@app.teardown_appcontext
def close_connection(ex):
    db = getattr(g, "_database", None)
    if db:
        db.close()


def get_all_table_names():
    connection = sqlite3.connect('app/app.db', check_same_thread=False)
    cursor = connection.cursor()
    tables = cursor.execute("SELECT name FROM sqlite_schema WHERE type ='table'")
    return tables.fetchall()
