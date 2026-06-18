from fastapi import APIRouter,HTTPException
from pydantic import BaseModel
from typing import Literal

from database.mission_db import MissionDB
from database.agent_db import AgentDB

adb = AgentDB() 
mdb = MissionDB()

router = APIRouter()
