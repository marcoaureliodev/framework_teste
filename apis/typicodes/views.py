from flask import request
from flask_apispec import MethodResource, doc
from flask_restful import Resource
from utils.helpers import auth_required
from apis.typicodes.services import Service


class Typicode(MethodResource, Resource):

    @doc(description="Typicodes namespace", tags=["Typicode"],
         security='apikey')
    @auth_required(request)
    def get(self):
        data_typicode_list = Service.get_data_typicode(self)
        return data_typicode_list, 200

