import csv
import sqlite3

conn = sqlite3.connect('trackdb.sqlite')
cur = conn.cursor()

# Start fresh each run
cur.executescript('''
DROP TABLE IF EXISTS Artist;
DROP TABLE IF EXISTS Genre;
DROP TABLE IF EXISTS Album;
DROP TABLE IF EXISTS Track;

CREATE TABLE Artist (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT UNIQUE
);

CREATE TABLE Genre (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT UNIQUE
);

CREATE TABLE Album (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    artist_id INTEGER,
    title TEXT UNIQUE
);

CREATE TABLE Track (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT UNIQUE,
    album_id INTEGER,
    genre_id INTEGER,
    len INTEGER, rating INTEGER, count INTEGER
);
''')

f = open('tracks.csv')
reader = csv.reader(f)
next(reader)  # skip header

for row in reader:
    name = row[0]
    artist = row[1]
    album = row[2]
    count = row[3]
    rating = row[4]
    length = row[5]
    genre = row[6]

    if not name:
        continue

    # Artist
    cur.execute('INSERT OR IGNORE INTO Artist (name) VALUES (?)', (artist,))
    cur.execute('SELECT id FROM Artist WHERE name=?', (artist,))
    artist_id = cur.fetchone()[0]

    # Genre
    cur.execute('INSERT OR IGNORE INTO Genre (name) VALUES (?)', (genre,))
    cur.execute('SELECT id FROM Genre WHERE name=?', (genre,))
    genre_id = cur.fetchone()[0]

    # Album
    cur.execute('INSERT OR IGNORE INTO Album (title, artist_id) VALUES (?, ?)',
                (album, artist_id))
    cur.execute('SELECT id FROM Album WHERE title=?', (album,))
    album_id = cur.fetchone()[0]

    # Track
    cur.execute('''
        INSERT OR REPLACE INTO Track
        (title, album_id, genre_id, len, rating, count)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (name, album_id, genre_id, length, rating, count))

conn.commit()
cur.close()
