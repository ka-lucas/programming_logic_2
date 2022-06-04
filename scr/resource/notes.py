from flask import request
from flask_restx import Resource

from scr.core.notes import NotesCore
from scr.resource.payload.notes import notes_ns, notes_payload

notes_core = NotesCore()


class Notes(Resource):
    @notes_ns.expect(notes_payload, validate=True)
    def post(self):
        data = request.get_json()
        result = notes_core.notes(data)
        return result
