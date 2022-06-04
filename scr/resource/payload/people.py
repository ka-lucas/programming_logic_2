from flask_restx import fields, Namespace

people_ns = Namespace('people')

# Payload
people_payload = people_ns.model('PeoplePayload', {
    'age': fields.Integer(required=True),
    'gender': fields.String(required=True)
}, strict=True)
