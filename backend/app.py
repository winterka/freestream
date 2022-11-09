from flask import Flask
from flask import render_template
from flask import request
from flask import send_file
from flask import jsonify
from models import get_tracks, post_track

app = Flask(__name__, template_folder='../frontend/dist', static_folder='../fronten/dist/assets')

@app.route("/", methods = ["GET","POST"])
def home():
    audio_source = '/home/winterec/Desktop/freestream/static/audio/3test.mp3'
    if request.method == "GET":
        pass
    if request.method == "POST":
        title = request.form.get('title')
        cover = request.form.get('cover')
        post_track(title, cover)
        tracks = get_tracks()
        return render_template('index.html', tracks = tracks)
    return jsonify(get_tracks())

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