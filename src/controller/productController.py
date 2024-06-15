from flask import Flask, request , Blueprint , jsonify
from ..service.productService import ProductService
from ..model.productModel import ReqProduct , Product
from ..model.model import Request
from pydantic_core import ValidationError
# from flask_pydantic import validate , ValidationError
import traceback

class ProductController:
    def __init__(self):
        self.__api = Blueprint('/api/v1' , __name__ , url_prefix='/api/v1')
        self.__service = ProductService()


    def GetRouter(self) -> Blueprint:
        @self.__api.route('/add' , methods=['POST'])
        def add():
            try:

                requestData:dict = request.get_json()
                product = ReqProduct.model_validate(requestData)
                result = self.__service.Upsert(product.model_dump() , False)
                return result , 201
            
            except ValidationError as err:
                traceback.print_exc()
                return {"error" : "validation error"}, 400
            
            except Exception as err:
                traceback.print_exc()
                return {"error" : "Intenal Server Error"} , 500

        @self.__api.route('/get-all' , methods=['POST'])
        def getAll():
            requestData = request.get_json()
            param = Request.model_validate(requestData)
            resp = self.__service.GetAll(param.model_dump())
            return resp , 200


        @self.__api.route('/get-one' , methods=['GET'])
        def getOne():
            param_id = request.args.get("id")
            response = self.__service.GetOne("id" , param_id)
            if not response:
                return {"massage" : "data is not found"} , 404
            return response


        @self.__api.route('/update' , methods=['PUT'])
        def update():
            try:

                requestData:dict = request.get_json()
                product = ReqProduct.model_validate(requestData)
                result = self.__service.Upsert(product.model_dump() , True)
                
                if not result:
                    return {"error" : "bad request"} , 400
                
                return result , 200
            
            except ValidationError as err:
                traceback.print_exc()
                return {"error" : "validation error"}, 400
            
            except Exception as err:
                traceback.print_exc()
                return {"error" : "Intenal Server Error"} , 500


        @self.__api.route('/delete' , methods=['DELETE'])
        def delete():
            param_id = request.args.get("id")
            response = self.__service.Delete("id" , param_id)
            return {"id" : response, "status" : True if response else False}
        
        return self.__api
