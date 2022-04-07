import inject
from acme_instruments_service.program.program_operations import ProgramOperations

program_operations = ProgramOperations()

def setup_depedencies():
    inject.configure(lambda binder: binder.bind(ProgramOperations, program_operations))
