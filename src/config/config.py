from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from ..model.model import Base
from ..util.pysql.pysql import PyMySQL

connection = PyMySQL.NewPyPGSQLUseEnv()
connection.InitEngine()
engine = connection.GetEngine()

def initEngine():
    Base.metadata.create_all(bind=engine)

sesion = connection.GetSesion()
