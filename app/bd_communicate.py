import sqlite3
from app import app
from flask import g


def add_question(question, ans1, ans2, correct):
    msg = ''
    connection = sqlite3.connect("app/app.db")
    cursor = connection.cursor()
    try:
        cursor.execute(f"""INSERT INTO chess_test
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


def get_all_tests():
    connection = sqlite3.connect("app/app.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * from chess_test")
    return cursor.fetchall()


@app.teardown_appcontext
def close_connection(ex):
    db = getattr(g, "_database", None)
    if db:
        db.close()
