from typing import List
from dataclasses import dataclass, field
from AcmeInstrumentsService.operation.operations import Operation
from AcmeInstrumentsService.program.program_id import ProgramId


@dataclass
class ProgramOperations:
    operations: List[Operation] = field(default_factory=list)
    id: ProgramId = ""
    counter: int = 0

    def add_operation(self, operation: Operation):
        if not isinstance(operation, Operation):
            raise TypeError(
                f"Operation type not recoginized {operation.__class__.__name__}"
            )
        self.operations.append(operation)

    def get_id(self) -> ProgramId():
        self.counter += 1
        self.id = f"AcmeProgramId{self.counter}"
        return self.id

    def clear(self):
        self.operations.clear()
