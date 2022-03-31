from pydantic import BaseModel, Field


class RunProgramResponse(BaseModel):
    result: int = Field(
        ...,
        description="A number representing the result of the program run",
        example="10",
    )
