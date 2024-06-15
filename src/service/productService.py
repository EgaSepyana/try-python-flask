from ..util.pysql.pysql import PyMySQL
from sqlalchemy.orm import Session
from ..model.productModel import Product
from .util import generate_uuid , fetch_result
from sqlalchemy import text
import json
from flask import jsonify


class ProductService:
   def __init__(self):
      self.__db = PyMySQL.NewPyPGSQLUseEnv()
      self.__db.InitEngine()
      self.__tableName = "products"

   def Upsert(self, data:dict , isUpdate:bool) -> str:
      if isUpdate:
         if not data.get("id"):
            return None
         resp = self.__db.UpdateDataUseModel(Product , data["id"] ,data)
         return resp
      
      data["id"] = generate_uuid()
      self.__db.AddDataUseModel(Product, data)
      return data

   def GetOne(self, key , value):
      resp = self.__db.GetOneUseModel(key , value , Product)
      if not resp:
         return None
      respAsDict = resp.__dict__.copy()
      del respAsDict["_sa_instance_state"]
      # print(resp)
      return respAsDict

   def GetAll(self, param:dict):
      session = self.__db.GetSesion()
      result = session.execute(text(f"SELECT * FROM {self.__tableName}"))
      return fetch_result(result)
      # return response

   def Delete(self,key , value):
      session = self.__db.GetSesion()
      session.execute(text(f"DELETE FROM {self.__tableName} WHERE {key} = '{value}' "))
      session.commit()
      return value