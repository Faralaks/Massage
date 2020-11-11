import sqlite3

db = sqlite3.connect('file:db.sqlite?mode=rwc', uri=True)
dbcursor  = db.cursor()

dbcursor.execute('''create table people (
                uid TEXT NOT NULL UNIQUE,
                count INTEGER  NOT NULL)''')
dbcursor.execute('''create table proc (
            uid TEXT NOT NULL,
            d INTEGER NOT NULL,
            m INTEGER NOT NULL,
            y INTEGER NOT NULL)''')

if 0:
    dbcursor.execute('''INSERT INTO people VALUES (?,?)''', ['Петров — 1А', 1])
    dbcursor.execute('''INSERT INTO people VALUES (?,?)''', ['Иванов — 3Б',7])
    dbcursor.execute('''INSERT INTO people VALUES (?,?)''', ['Сергеев — 3Б',10])
    dbcursor.execute('''INSERT INTO people VALUES (?,?)''', ['Семенов — 8Г', 1])
    dbcursor.execute('''INSERT INTO people VALUES (?,?)''', ['Курочкин — 1А', 0])



            
db.commit()
db.close()
























