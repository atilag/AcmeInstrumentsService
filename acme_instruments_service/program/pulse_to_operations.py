from typing import List
from acme_instruments_service.pulse.pulse import Pulse
from acme_instruments_service.operation.operations import (
    Multiplication,
    Division,
    Summation,
    SetInitialState,
)
from acme_instruments_service.program.errors import InvalidPulseSequenceError

_PULSES_TO_OPERATION = {
    (Pulse.AcmePulse1, Pulse.AcmePulse2): Summation,
    (Pulse.AcmePulse2, Pulse.AcmePulse1, Pulse.AcmePulse1): Multiplication,
    (Pulse.AcmePulse2, Pulse.AcmePulse2): Division,
    (Pulse.AcmeInitialStatePulse,): SetInitialState,
}


def from_pulse_sequence_to_operation(pulses: List[Pulse], value: int):
    pulse_sequence_types = tuple(pulses)
    try:
        OperationType = _PULSES_TO_OPERATION[pulse_sequence_types]
    except KeyError:
        raise InvalidPulseSequenceError(
            f"There's no existing operation for this pulse sequence: {pulse_sequence_types}"
        )

    return OperationType(
        value=value
    )  # Create an instance of the operation with its corresponding value