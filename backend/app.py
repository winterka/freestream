from flask import Flask
from flask import render_template
from flask import request
from flask import send_file
from flask import jsonify
from flask import send_from_directory
from models import get_tracks, post_track

app = Flask(__name__, template_folder='../frontend/dist', static_folder='../frontend/dist/assets')

@app.route("/", methods = ["GET","POST"])
def home():
    if request.method == "GET":
        pass
    if request.method == "POST":
        title = request.form.get('title')
        cover = request.form.get('cover')
        post_track(title, cover)
        return render_template('index.html', tracks = get_tracks())
    return render_template('index.html', tracks = get_tracks())

@app.route('/api/get-tracks',methods = ['GET'])
def get_tracks_json():
    return jsonify(get_tracks())

@app.route('/<path:path>', methods = ["GET"])
def get_cover(path):
    if path.endswith('.jpg'):
        return send_from_directory(
            directory = 'src/',
            path = path
        )
    if path.endswith('.mp3'):
        return send_from_directory(
           directory= 'src/audio',
           path = path
        )

if __name__ == '__main__':
    app.run(debug=True)