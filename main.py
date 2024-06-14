from flask import Flask, request , Blueprint
import ast
import json
from src.config.config import initEngine
from src.controller.productController import ProductController
from route import api
import util as ut

initEngine()

app = Flask(__name__)  

product_controller = ProductController().GetRouter()

app.register_blueprint(product_controller)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")