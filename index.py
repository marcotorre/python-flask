from flask import Flask, render_template, __version__
app = Flask(__name__)
source = 'https://github.com/marcotorre/python-flask'
css = '<link rel="stylesheet" href="/css/style.css" />'

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return render_template("index.html", css=css, source=source)
