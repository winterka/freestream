from flask import Flask
from flask import render_template
from flask import send_from_directory
from flask import request
from flask import send_file
from models import get_tracks, post_track

app = Flask(__name__, template_folder='../frontend/templates')

@app.route("/", methods = ["GET","POST"])
def home():
    audio_source = '/home/winterec/Desktop/freestream/static/audio/3test.mp3'
    if request.method == "GET":
        pass
    if request.method == "POST":
        title = request.form.get('title')
        post_track(title, audio_source)
        tracks = get_tracks()
        return render_template('index.html', tracks = tracks)
    return render_template('index.html')


@app.route('/<audio_file_name>')
def send_track(audio_file_name):
    path_to_audio_file = "/home/winterec/Desktop/freestream/static/audio/" + audio_file_name
    return send_file(
         path_to_audio_file, 
         mimetype="audio/mpeg", 
         as_attachment=True, 
         download_name="zzz.mp3")

if __name__ == '__main__':
    app.run(debug=True)