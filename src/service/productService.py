from ..util.pysql.pysql import PyMySQL
from sqlalchemy.orm import Session
from ..model.productModel import Product
from .util import generate_uuid

class ProductService:
   def __init__(self):
      self.__db = PyMySQL.NewPyPGSQLUseEnv()
      self.__db.InitEngine()

   def Upsert(self, data:dict , isUpdate:bool) -> str:
      data["id"] = generate_uuid()
      self.__db.AddDataUseModel(Product,data)
      return data.get("id")

   def GetOne(self, key , value):
      pass

   def GetAll(self,param):
      pass

   def Delete(self,key , value):
      pass