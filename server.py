from flask import Flask, jsonify
from flask_cors import CORS
import mysql.connector

app = Flask(__name__)
CORS(app)

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="spotify_clone"
)

@app.route('/songs')
def get_songs():
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM songs")
    songs = cursor.fetchall()
    cursor.close()
    return jsonify(songs)

@app.route('/featured-songs')
def get_featured_songs():
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM songs LIMIT 5")
    featured_songs = cursor.fetchall()
    cursor.close()
    return jsonify(featured_songs)

@app.route('/albums')
def get_albums():
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM albums")
    albums = cursor.fetchall()
    cursor.close()
    return jsonify(albums)


if __name__ == '__main__':
    app.run(debug=True)
