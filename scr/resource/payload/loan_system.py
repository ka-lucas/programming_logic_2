from flask_restx import fields, Namespace

loan_system_ns = Namespace('loan-system')

loan_system_payload = loan_system_ns.model('LoanSystemPayload', {
    'house_value': fields.Integer(required=True),
    'salary': fields.Integer(required=True),
    'years': fields.Integer(required=True)
}, strict=True)
