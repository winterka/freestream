import sqlite3 as sql
from os import path

ROOT = path.dirname(path.relpath((__file__)))

def post_track(title, source_audio):
    cover = 'cover1.jpg'
    con = sql.connect(path.join(ROOT, 'database.db'))
    cur = con.cursor()
    cur.execute('INSERT INTO tracks (title, source_audio, cover) VALUES (?, ?, ?)', (title, source_audio, cover))
    con.commit()
    con.close()

def get_tracks():
    con = sql.connect(path.join(ROOT, 'database.db'))
    cur = con.cursor()
    cur.execute('SELECT * FROM tracks')
    tracks = cur.fetchall()
    return tracks