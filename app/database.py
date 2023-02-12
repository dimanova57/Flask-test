import sqlite3

connect = sqlite3.connect("app.db")
print("Created")
cursor = connect.cursor()
print("Cursor Created")

cursor.execute("""CREATE TABLE chess_test 
                    (question TEXT, ans1 TEXT, ans2 TEXT, correct TEXT)""")
connect.close()
print("Table created")
