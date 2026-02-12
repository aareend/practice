import json
import sqlite3

conn = sqlite3.connect('roster.sqlite')
cur = conn.cursor()

cur.executescript('''
DROP TABLE IF EXISTS User;
DROP TABLE IF EXISTS Course;
DROP TABLE IF EXISTS Member;

CREATE TABLE User (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT UNIQUE
);

CREATE TABLE Course (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT UNIQUE
);

CREATE TABLE Member (
    user_id INTEGER,
    course_id INTEGER,
    role INTEGER,
    PRIMARY KEY (user_id, course_id)
);
''')

# Load JSON
fname = 'roster_data.json'
data = json.load(open(fname))

for entry in data:
    name = entry[0]
    title = entry[1]
    role = entry[2]

    # User
    cur.execute('INSERT OR IGNORE INTO User (name) VALUES (?)', (name,))
    cur.execute('SELECT id FROM User WHERE name=?', (name,))
    user_id = cur.fetchone()[0]

    # Course
    cur.execute('INSERT OR IGNORE INTO Course (title) VALUES (?)', (title,))
    cur.execute('SELECT id FROM Course WHERE title=?', (title,))
    course_id = cur.fetchone()[0]

    # Member (THIS IS THE PART YOU MUST ADD)
    cur.execute('''
        INSERT OR REPLACE INTO Member (user_id, course_id, role)
        VALUES (?, ?, ?)
    ''', (user_id, course_id, role))

conn.commit()
cur.close()
