from flask import Flask
from models import initDatabase
from flask import render_template

app = Flask(__name__)

@app.route('/')
def index():
    initDatabase()
    return "Hello world !"

@app.route('/test')
def test():
    return render_template('melissa.html')

if __name__ == "__main__":
    app.run()