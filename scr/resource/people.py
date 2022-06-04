from flask import request
from flask_restx import Resource

from scr.core.people import PeopleCore
from scr.resource.payload.people import people_payload, people_ns

people_core = PeopleCore()


class People(Resource):
    @people_ns.expect([people_payload], validate=True)
    def post(self):
        data = request.get_json()
        result = people_core.analysis(data)
        return result
