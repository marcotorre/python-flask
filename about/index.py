from flask import Flask, render_template, __version__
app = Flask(__name__)
source = 'https://github.com/marcotorre/python-flask'
css = '/css/style.css'

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    name = path.upper()
    v = __version__
    return render_template("about.html", css=css, name=name, v=v, source=source)
