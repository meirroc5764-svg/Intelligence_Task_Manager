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

class UpAgent(BaseModel):
    name:str|None = None 
    specialty:str|None = None  
    is_active:bool|None = None
    completed__missions:int|None = None
    failed_missions:int|None = None
    agent_ran:int|None = None


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
    my_agent = adb.get_agent_by_id(id)
        
    if my_agent == None:
        raise HTTPException(status_code=404,detail="not found")
        
    return {"the agent":my_agent}

    


@router.put("/agents/{id}",status_code=200)
def update_agent(id:int,data:UpAgent):
    try:
        my_agent = adb.update_agent(id,data.model_dump(exclude_none=True))
        return {"message":my_agent}
    except:
        raise HTTPException(status_code=500,detail="false")


@router.put("/agents/{id}/deactivate",status_code=200)
def deactive_agents(id:int):
    try:
        my_agent = adb.deactivate_agent(id)
        return {"message":my_agent}
    except:
        raise HTTPException(status_code=500,detail="deactive false")
    

@router.get("/agents/{id}/performance")
def agents_performance(id:int):
    try:
        return adb.get_agent_performance(id)
    except Exception as e:
        raise HTTPException(status_code=500,detail=str(e))