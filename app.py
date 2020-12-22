from flask import Flask, render_template, url_for, redirect, request
from fastai.text.all import *
import sentencepiece

ORT = int(os.environ.get('PORT', 5000))

app = Flask(__name__)
app.config.from_object(__name__)

# load model
learn_inf = load_learner("genreModel.pkl")

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/lyrics", methods=["POST"])
def lyrics():
    lyrics = request.form["lyrics"]
    pred = learn_inf.predict(lyrics)[0]

    # edit string output
    if pred == "hiphop":
        pred = "Hip-Hop"
    if pred in ["pop", "schlager"]:
        pred = pred.capitalize()

    if pred == "Hip-Hop":
        return render_template("hiphop.html", pred=pred)
    if pred == "Pop":
        return render_template("pop.html", pred=pred)
    if pred == "Schlager":
        return render_template("schlager.html", pred=pred)




    # if not artist:
    #     return redirect(url_for("index"))
    #
    # if not artist in ["Kool Savas", "Helene Fischer"]:
    #     return "Diese App unterstützt derzeit nur Lyrics für Kool Savas und Helene Fischer. Bitte passe den Künstler an!"
    #
    return render_template("lyrics.html", pred=pred)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=PORT)
