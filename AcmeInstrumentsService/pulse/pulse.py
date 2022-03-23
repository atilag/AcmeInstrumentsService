from enum import Enum, IntEnum


class Pulse(str, Enum):
    AcmePulse1 = "Acme_pulse_1"
    AcmePulse2 = "Acme_pulse_2"
    AcmePulse3 = "Acme_pulse_3"
    AcmeInitialStatePulse = "Acme_initial_state_pulse"
