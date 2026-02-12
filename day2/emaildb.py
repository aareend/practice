import sqlite3

conn = sqlite3.connect('orgcounts.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Counts')
cur.execute('CREATE TABLE Counts (org TEXT, count INTEGER)')

fh = open('mbox.txt')

for line in fh:
    if not line.startswith('From: '):
        continue

    email = line.split()[1]
    domain = email.split('@')[1]

    cur.execute('SELECT count FROM Counts WHERE org = ?', (domain,))
    row = cur.fetchone()

    if row is None:
        cur.execute('INSERT INTO Counts (org, count) VALUES (?, 1)', (domain,))
    else:
        cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?', (domain,))

conn.commit()
cur.close()
