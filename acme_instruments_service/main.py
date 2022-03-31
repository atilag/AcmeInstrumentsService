from typing import Optional

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from acme_instruments_service.program.program_id import ProgramId
from acme_instruments_service.program.load.load_program import load_program
from acme_instruments_service.program.load.load_program_response import LoadProgramResponse
from acme_instruments_service.program.load.load_program_request import LoadProgramRequest
from acme_instruments_service.program.run.run_program import run_program
from acme_instruments_service.program.run.run_program_response import RunProgramResponse
from acme_instruments_service.program.errors import (
    InvalidPulseSequenceError,
    ValueNotAnIntegerError,
    MalformedProgramError,
    ProgramNotFoundError,
    DivisionByZeroError,
)

from .dependencies import setup_depedencies

app = FastAPI()

setup_depedencies()


@app.post("/load_program", response_model=LoadProgramResponse, status_code=200)
def load_program_endpoint(program_req: LoadProgramRequest):
    program_id = load_program(program_req.program_code)
    return LoadProgramResponse(program_id=program_id)


@app.get(
    "/run_program/{program_id}", response_model=RunProgramResponse, status_code=200
)
def run_program_endpoint(program_id: ProgramId):
    result = run_program(program_id)
    return RunProgramResponse(program_id=program_id, result=result.result)


@app.exception_handler(InvalidPulseSequenceError)
async def invalid_pulse_sequence_exception_handler(
    request: Request, ex: InvalidPulseSequenceError
):
    return JSONResponse(
        status_code=452,
        content={"message": f"{ex.name}"},
    )


@app.exception_handler(ValueNotAnIntegerError)
async def value_not_an_integer_exception_handler(
    request: Request, ex: ValueNotAnIntegerError
):
    return JSONResponse(
        status_code=453,
        content={"message": f"{ex.name}"},
    )


@app.exception_handler(MalformedProgramError)
async def malformed_program_exception_handler(
    request: Request, ex: MalformedProgramError
):
    return JSONResponse(
        status_code=454,
        content={"message": f"{ex.name}"},
    )


@app.exception_handler(ProgramNotFoundError)
async def program_not_found_exception_handler(
    request: Request, ex: ProgramNotFoundError
):
    return JSONResponse(
        status_code=455,
        content={"message": f"{ex.name}"},
    )


@app.exception_handler(DivisionByZeroError)
async def division_by_zero_exception_handler(request: Request, ex: DivisionByZeroError):
    return JSONResponse(
        status_code=456,
        content={"message": f"{ex.name}"},
    )
