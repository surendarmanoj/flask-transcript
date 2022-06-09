from crypt import methods
from tkinter.messagebox import NO
from flask import Flask, redirect, render_template, request
import speech_recognition as sr
app = Flask(__name__)

@app.route("/", methods=['GET','POST'])
def home():
    text=""
    if request.method == "POST":
        print("Data recieved")
        if "file" not in request.files:
            return redirect(request.url)

        file = request.files['file']
        if file.filename == "":
            return redirect(request.url)

        if file:
            recognizer = sr.Recognizer()
            audioFile = sr.AudioFile(file)
            with audioFile as source:
                data = recognizer.record(source)
            text = recognizer.recognize_google(data, key=None)
            print(text)
    else:
        return render_template("index.html")
    return render_template("index.html",transcript=text)

if __name__ == "__main__":
    app.run(debug=True, threaded=True)