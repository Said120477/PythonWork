from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

notes_list = [
    {'id': 1, 'text': 'заметка 1'},
    {'id': 2, 'text': 'надо купить хлеб'}
]
@app.route("/notes")
def notes():
    return render_template('notes.html', notes_list=notes_list)