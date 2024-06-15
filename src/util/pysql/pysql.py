import os
# from model.model import URL , Source
from uuid import uuid4
from sqlalchemy import create_engine , Engine , delete
from sqlalchemy.orm import Session
from dotenv import load_dotenv
import traceback

load_dotenv()

class PyMySQL:
    _engine:Engine = None
    _sesion:Session = None

    driverDb = {
        "mysql" : "mysqlconnector",
        "postgresql" : "psycopg2"
    }

    def __init__(self , host , user , db ,password="" , dbType = "mysql"):
        self.host = host
        self.user = user
        self.password =password
        self.db = db
        self.dbType = dbType

    @classmethod
    def NewPyMySQLUseEnv(cls):
        return cls(os.getenv("DATABASE_HOST") ,os.getenv("DATABASE_USERNAME") , os.getenv("DATABASE_NAME") , os.getenv("DATABASE_PASSWORD") , "mysql")
    
    @classmethod
    def NewPyPGSQLUseEnv(cls):
        return cls(os.getenv("DATABASE_HOST") ,os.getenv("DATABASE_USERNAME") , os.getenv("DATABASE_NAME") , os.getenv("DATABASE_PASSWORD") , "postgresql")
 

    @classmethod
    def NewPyMySQLLocal(cls):
        return cls("localhost" ,"root" , "" , "default" , "mysql")

    def SetTable(self , tableName):
        self.table = tableName
    
    def InitEngine(self):
        self._engine = create_engine(f"{self.dbType}+{self.driverDb[self.dbType]}://{self.user}:{self.password}@{self.host}/{self.db}")
        self._sesion = Session(bind=self._engine)

    def GetSesion(self):
        return self._sesion     

    def GetEngine(self):
        return self._engine   

    def AddDataUseModel(self, Model , data:dict):
        self._sesion.add(Model(**data))
        self._sesion.commit()
    
    def CloseConnection(self):
        self._sesion.close()
    
    def GetOneUseModel(self , key , value, Model):
        source = self._sesion.query(Model).filter_by(**{key : value})
        return source.first()
    
    def UpdateDataUseModel(self, Model , id:str , data:dict):
        datum = self._sesion.query(Model).filter_by(id=id)
        
        if datum.first():
            if data.get("id"):
                del data["id"]
            data["id"] = datum.first().id
            datum.update(data , synchronize_session=False)
            self._sesion.commit()
            self._sesion.refresh(datum.first())
            return data
        else:
            print("Data Does't Exist")

    