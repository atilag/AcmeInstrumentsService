from typing import Union, List
import inject
from AcmeInstrumentsService.program.program_id import ProgramId
from AcmeInstrumentsService.pulse.pulse import Pulse
from AcmeInstrumentsService.program.program_operations import ProgramOperations
from AcmeInstrumentsService.program.pulse_to_operations import (
    from_pulse_sequence_to_operation,
)


@inject.params(operations=ProgramOperations)
def load_program(
    program_code: List[Union[Pulse, int]], operations: ProgramOperations
) -> ProgramId:
    """Load the ACME pulse representation and translate it into a sequence of arithmetic operations"""
    operations.clear()  # We only run one program at a time, so we remove previous operations everytime a new
    # program arrives.
    pulse_block = []
    # A block of pulses is defined by a sequence of pusles plus a value that ends the block
    for pulse_or_value in program_code:
        if isinstance(pulse_or_value, Pulse):
            pulse_block.append(pulse_or_value)
        elif isinstance(pulse_or_value, int):
            operations.add_operation(
                from_pulse_sequence_to_operation(pulse_block, pulse_or_value)
            )
            pulse_block.clear()

    return operations.get_id()
