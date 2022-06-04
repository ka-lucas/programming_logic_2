from flask_restx import Namespace, fields

# Namespace
table_ns = Namespace('table')

# Payload
table_payload = table_ns.model('TablePayload', {
    'number': fields.Integer(required=True)
},strict=True)
