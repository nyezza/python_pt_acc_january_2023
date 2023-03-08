from flask import redirect, render_template, request
from flask_app import app
from flask_app.models.song_model import Song
from flask_app.models.singer_model import Singer


@app.route('/songs')
def all_songs():
    songs = Song.get_all()
    return render_template("all_songs.html", songs  = songs)

@app.route('/songs/new')
def new_song():
    all_singers = Singer.get_all()
    return render_template("new_song.html" ,all_singers = all_singers)