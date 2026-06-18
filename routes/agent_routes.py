from fastapi import APIRouter,HTTPException
from pydantic import BaseModel
from typing import Literal

from database.agent_db import AgentDB 

router = APIRouter()

adb = AgentDB()

class CNewAgent(BaseModel):
    name:str 
    specialty:str 
    agent_rank:Literal['Junior','Senior','Commandor']


@router.post("/agents",status_code=201)
def create_agent(data:CNewAgent):
    if not BaseModel:
        raise HTTPException(status_code=422,detail="not a validate value")
    try:
        new_agent = adb.create_agent(data.model_dump())
        
        return {"create a agent":new_agent}
    except:
        raise HTTPException(status_code=500, detail="create false")
    

@router.get("/agents")
def show_all():
    try:
        all_data = adb.get_all_agents()
        return all_data
    except:
        raise HTTPException(status_code=500,detail="false")
    
@router.get("/agents/{id}")
def find_by_id(id:int):
    if not int(id):
        raise HTTPException(status_code=422,detail="eror value")
    try:
        my_agent = adb.get_agent_by_id(id)
        if not my_agent:
            return []
        return {"the agent":my_agent}
    except:
        raise HTTPException(status_code=500,detail="false")