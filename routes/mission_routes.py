from fastapi import APIRouter,HTTPException
from pydantic import BaseModel
from typing import Literal

from database.mission_db import MissionDB
from database.agent_db import AgentDB

adb = AgentDB() 
mdb = MissionDB()

router = APIRouter()

class CreateMissions(BaseModel):
    scription:str 
    locatitle:str 
    detion:str
    difficulty:int 
    importance:int




@router.post("/missions",status_code=201)
def create_missions(data:CreateMissions):
    try:
       return mdb.create_mission(data.model_dump())
    except:
        raise HTTPException(status_code=500,detail="create false")
    
@router.get("/missions",status_code=200)
def show_all():
    try:
        all_data = mdb.get_all_missions()
        if not all_data:
            return []
        return all_data
    except Exception as e:
        raise HTTPException(status_code=500,detail=str(e))
    

@router.get("/missions/{id}")
def find_by_id(id:int):
    my_mission = mdb.get_mission_by_id(id)
    if not my_mission:
        raise HTTPException(status_code=404,detail="not found")
    return my_mission

@router.put("/missions/{id}/assign/{agent_id}")
def assign_mission(mission_id:int, agent_id:int):
            
    if not adb.get_agent_by_id(agent_id):
            raise HTTPException(status_code=404,detail="not fount a agent with this id")
        
    if not mdb.get_mission_by_id(mission_id):
            raise HTTPException(status_code=404,detail="not found a mission with this id")
    
    return mdb.assign_mission(mission_id, agent_id)

@router.put("/missions/{id}/start",status_code=200)
def start_status(id,status:Literal["ASSIGNED","IN_PROGRESS"]):
    
    if not mdb.get_mission_by_id(id):
        raise HTTPException(status_code=404,detail="not found a mission with this id")
    try:
        return mdb.update_mission_status(id,status)
    except Exception as e:
        raise HTTPException(status_code=500,detail=str(e))
    
@router.put("/missions/{id}/complete",status_code=200)
def mission_complite(id):
    if not mdb.get_mission_by_id(id):
        raise HTTPException(status_code=404,detail="not found a mission with this id")
    try:
        return mdb.update_mission_status(id,"complete")
    
    except Exception as e:
        raise HTTPException(status_code=500,detail=str(e))
    
@router.put("/missions/{id}/failed")
def mission_failed(id):
    if not mdb.get_mission_by_id(id):
        raise HTTPException(status_code=404,detail="not found a mission with this id")
    try:
        return mdb.update_mission_status(id,"FAILED")
    
    except Exception as e:
        raise HTTPException(status_code=500,detail=str(e))
    

@router.put("/missions/{id}/cancel")
def mission_failed(id):
    if not mdb.get_mission_by_id(id):
        raise HTTPException(status_code=404,detail="not found a mission with this id")
    try:
        return mdb.update_mission_status(id,"CANCELLED")
    
    except Exception as e:
        raise HTTPException(status_code=500,detail=str(e))

