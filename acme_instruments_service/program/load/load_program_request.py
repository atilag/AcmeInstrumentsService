from pydantic import BaseModel, Field
from typing import List, Union
from acme_instruments_service.pulse.pulse import Pulse


class LoadProgramRequest(BaseModel):
    program_code: List[Union[Pulse, int]] = Field(
        ...,
        description="An ACME-specific pulse sequence representation of a quantum program",
        exmaple="['AcmePulse1','AcmePulse2','120']",
    )
