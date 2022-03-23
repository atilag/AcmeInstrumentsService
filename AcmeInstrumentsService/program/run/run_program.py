import operator
import inject
from AcmeInstrumentsService.program.program_operations import ProgramOperations
from AcmeInstrumentsService.program.run.ProgramResult import ProgramResult
from AcmeInstrumentsService.program.program_id import ProgramId


@inject.params(operations=ProgramOperations)
def run_program(program_id: ProgramId, operations: ProgramOperations) -> ProgramResult:
    """Run program use case!"""
    result = 0
    for operation in operations.operations:
        result = operation.operator(result, operation.value)

    return ProgramResult(result=result)
