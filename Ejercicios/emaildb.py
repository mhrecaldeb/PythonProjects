import sqlite3 # la libreria

conn = sqlite3.connect('emaildb.sqlite') #abrir la conexion
cur = conn.cursor()  #crear el manejador al que se envian las instrucciones SQL

cur.execute('''
DROP TABLE IF EXISTS Counts''') # elimino la tabla en caso que exista para comenzar de cero

cur.execute('''
CREATE TABLE Counts (email TEXT, count INTEGER)''') # creamos la tabla y sus campos

fname = input("Enter file name: ")

direct = 'C:/Users/mhrec/PythonProjects/Freecodecamp-Python/code3/'

if (len(fname) < 1): fname = 'mbox-short.txt'

fh = open(direct + '/' + fname)

for line in fh:

    if not line.startswith('From: '): continue

    pieces = line.split()
    email = pieces[1]

    cur.execute('SELECT count FROM Counts WHERE email = ? ', (email,))
    row = cur.fetchone()

    if row is None:
        cur.execute('''INSERT INTO Counts (email, count)
                VALUES (?, 1)''', (email,))

    else:
        cur.execute('UPDATE Counts SET count = count + 1 WHERE email = ?', (email, ) )

    conn.commit()

# https://www.sqlite.org/lang_select.html
sqlstr = 'SELECT email, count FROM Counts ORDER BY count DESC LIMIT 10'

for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])
