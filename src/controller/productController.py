from flask import Flask, request , Blueprint , jsonify
from ..service.productService import ProductService
from ..model.productModel import ReqProduct , Product
from flask_pydantic import validate , ValidationError
import traceback

class ProductController:
    def __init__(self):
        self.__api = Blueprint('/api/v1' , __name__ , url_prefix='/api/v1')
        self.__service = ProductService()


    def GetRouter(self) -> Blueprint:
        @self.__api.route('/add' , methods=['POST'])
        def add():
            try :

                requestData:dict = request.get_json()
                product = ReqProduct.model_validate(requestData)
                self.__service.Upsert(product.model_dump() , False)
                return product.model_dump() , 201
            
            except ValidationError as err:
                traceback.print_exc()
                return {"error" : "error"}, 400
            
            except Exception as err:
                traceback.print_exc()
                return {"error" : "Intenal Server Error"} , 500

        @self.__api.route('/get-all' , methods=['POST'])
        def getAll():
            requestData = request.get_json()
            return {
                "func" : "get-all"
            }


        @self.__api.route('/get-one' , methods=['GET'])
        def getOne():
            requestData = request.get_json()
            return {
                "func" : "get-one"
            }


        @self.__api.route('/update' , methods=['PUT'])
        def update():
            requestData = request.get_json()
            return {
                "func" : "update"
            }


        @self.__api.route('/delete' , methods=['DELETE'])
        def delete():
            requestData = request.get_json()
            return {
                "func" : "delete"
            }
        
        return self.__api
