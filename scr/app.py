from flask import Flask
from flask_restx import Api

from scr.resource.loan_system import LoanSystem
from scr.resource.notes import Notes
from scr.resource.payload.loan_system import loan_system_ns
from scr.resource.payload.notes import notes_ns
from scr.resource.payload.people import people_ns
from scr.resource.payload.table import table_ns
from scr.resource.people import People
from scr.resource.table import Table

# configs
app = Flask(__name__)
api = Api(app)

# namespaces
api.add_namespace(table_ns)
api.add_namespace(loan_system_ns)
api.add_namespace(people_ns)
api.add_namespace(notes_ns)

# route
table_ns.add_resource(Table, '')
loan_system_ns.add_resource(LoanSystem, '')
people_ns.add_resource(People, '')
notes_ns.add_resource(Notes, '')