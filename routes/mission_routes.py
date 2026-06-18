from fastapi import APIRouter,HTTPException
from pydantic import BaseModel
from typing import Literal


router = APIRouter()


@router.post("/missions")
def create_missions(data):
    pass