import sqlite3
conn = sqlite3.connect("bayreach.sqlite")
c = conn.cursor()
c.execute('''CREATE TABLE users
                    (name text, hours real)''')