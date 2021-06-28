from flask import Flask, render_template, request
from models import db, Classe

app = Flask(__name__)

app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:root@localhost/tutore'
db.init_app(app)

@app.route('/')
def listeClasses():
    return render_template('melissa.html')

@app.route('/nouvelleClasse', methods=['POST'])
def nouvelleClasse():
    if request.method == 'POST':
        nomDeLaClasse = request.form['nom']
        print("La valeur est : " + nomDeLaClasse)
        db.session.add(Classe(nom=nomDeLaClasse))
        db.session.commit
        return "Sauvegarde reussie"

if __name__ == "__main__":
    app.run()