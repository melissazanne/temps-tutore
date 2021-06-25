from sqlalchemy import create_engine
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, Text, DateTime, ForeignKey
from sqlalchemy.orm import declarative_base

import logging as lg

Base = declarative_base()
# Create database connection object
engine = create_engine('postgresql+psycopg2://postgres:root@localhost/tutore')

class Classe(Base):
    __tablename__ = 't_classe'

    id = Column(Integer, primary_key=True)
    nom = Column(Text)
    sessions = relationship("Session")

    def __init__(self, nom):
        self.nom = nom

        
class Manager(Base):
    __tablename__ = 't_manager'

    id = Column(Integer, primary_key=True)
    nom = Column(Text)
    prenom = Column(Text)

    def __init__(self, prenon, nom):
        self.nom = nom
        self.prenom = prenom

class Session(Base):
    __tablename__ = 't_session'

    id = Column(Integer, primary_key=True)
    nom = Column(Text)
    fin = Column(DateTime)
    debut = Column(DateTime)
    classe_id = Column(Integer, ForeignKey('t_classe.id'))
    
    def __init__(self, nom, debut, fin ):
        self.nom =nom
        self.fin = fin
        self.debut = debut

def initDatabase():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
    lg.warning('Database is ok')