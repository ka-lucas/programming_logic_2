from flask_restx import Namespace, fields

notes_ns = Namespace('notes')

# Payload
notes_payload = notes_ns.model('NotesPayload', {
    'numbers': fields.List(fields.Integer(required=True), required=True)
}, strict=True)
