import sqlite3
con=sqlite3.connect('654.db')
print(con)
cur=con.cursor()
f=cur.execute('SELECT * FROM computers')
print(f.fetchall())
cur.execute("INSERT INTO computers ('mark', 'modal') VALUES ('Apple', 'Mac')")

con.commit()