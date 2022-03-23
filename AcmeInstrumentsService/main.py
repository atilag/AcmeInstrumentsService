from typing import Optional

from fastapi import FastAPI

from AcmeInstrumentsService.program.program_id import ProgramId
from AcmeInstrumentsService.program.load.load_program import load_program
from AcmeInstrumentsService.program.load.LoadProgramResponse import LoadProgramResponse
from AcmeInstrumentsService.program.load.LoadProgramRequest import LoadProgramRequest
from AcmeInstrumentsService.program.run.run_program import run_program
from AcmeInstrumentsService.program.run.RunProgramResponse import RunProgramResponse
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
