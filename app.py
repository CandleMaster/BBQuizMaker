from flask import Flask, render_template, request
from processing import find_questions

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        video_id = request.form['video-ids']
        return find_questions(video_id)
    #  pass video_id into processing
    return render_template('index.html')



if __name__=="__main__":
    app.run(debug=True)