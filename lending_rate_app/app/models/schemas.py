from pydantic import BaseModel
from typing import List, Optional


class ModeLInput(BaseModel):
    inflation: List[int]
    economic_growth: List[float]


class ModeLOutput(BaseModel):
    result: List[float]
