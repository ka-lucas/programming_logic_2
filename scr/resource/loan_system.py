from flask import request
from flask_restx import Resource

from scr.core.loan_system import LoanSystemCore
from scr.resource.payload.loan_system import loan_system_payload, loan_system_ns

loan_system_core = LoanSystemCore()


class LoanSystem(Resource):
    @loan_system_ns.expect(loan_system_payload, validate=True)
    def post(self):
        data = request.get_json()
        result = loan_system_core.calculate(data)
        return result
