from flask import Flask, render_template, request, redirect
from models import db, Classe, Session

app = Flask(__name__)

app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:root@localhost/tutore'
db.init_app(app)

# Views for CRUD Manager interface
@app.route("/")
def listeClasses():
    classes = Classe.query.all()
    return render_template("melissa.html", listeDesClasses=classes)

@app.route("/nouvelleClasse", methods=["POST"])
def nouvelleClasse():
    if request.form:
        newClasse = Classe(nom=request.form.get("nom"))
        db.session.add(newClasse)
        db.session.commit()
    return redirect("/")

@app.route("/modifierClasse/<classeID>", methods=["GET"])
def formulaireModifierClasse(classeID):
    if request.method == "GET":
        classe = Classe.query.filter_by(id=classeID).first()
    return render_template("modifierClasse.html", classToBeUpdated=classe)

@app.route("/modifierClasse", methods=["POST"])
def modifierClasse():
    if request.form:
        classeID = request.form.get("id")
        classe = Classe.query.filter_by(id=classeID).first()
        classe.nom = request.form.get("nom")
        db.session.commit()
    return redirect("/")

@app.route("/supprimerClasse/<classeID>", methods=["GET"])
def supprimerClasse(classeID):
    if request.method == "GET":
        classe = Classe.query.filter_by(id=classeID).first()
        db.session.delete(classe)
        db.session.commit()
    return redirect("/")

@app.route("/sessions/<classeID>")
def sessionsParClasse(classeID):
    classe = Classe.query.filter_by(id=classeID).first()
    return render_template("sessions.html", classe=classe, listeDesSessions=classe.sessions)

@app.route("/nouvelleSession", methods=["POST"])
def nouvelleSession():
    if request.form:
        newSession = Session(nom=request.form.get("nom"), debut=request.form.get("debut"), fin=request.form.get("fin"))
        classeID = request.form.get("classeID")
        newSession.classe_id = classeID

        db.session.add(newSession)
        db.session.commit()
    return redirect("/")

@app.route("/supprimerSession/<sessionID>", methods=["GET"])
def supprimerSession(sessionID):
    if request.method == "GET":
        session = Session.query.filter_by(id=sessionID).first()
        db.session.delete(session)
        db.session.commit()
    return redirect("/")

if __name__ == "__main__":
    app.run()