from flask import request
from flask_restx import Resource

from scr.core.table import TableCore
from scr.resource.payload.table import table_payload, table_ns

table_core = TableCore()


class Table(Resource):
    @table_ns.expect(table_payload, validate=True)
    def post(self):
        data = request.get_json()
        result = table_core.calculate(data)
        return result
