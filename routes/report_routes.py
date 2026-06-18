from fastapi import APIRouter,HTTPException
from pydantic import BaseModel
from typing import Literal

from database.mission_db import MissionDB
from database.agent_db import AgentDB

adb = AgentDB() 
mdb = MissionDB()

router = APIRouter()

@router.get("/summary/reports",status_code=200)
def summary():
    active = adb.count_active_agents()
    total_missions = mdb.count_all_missions()
    open_missions = mdb.count_open_missions()
    completed_missions = mdb.count_by_status("COMPLETED")
    failed_missions = mdb.count_by_status("FAILED")
    critical_missions = mdb.count_critical_missions()
    return{
"active_agents_count": active,
"total_missions": total_missions,
"open_missions": open_missions,
"completed_missions": completed_missions,
"failed_missions": failed_missions,
"critical_missions": critical_missions
}

@router.get("/reports/missions-by-status",status_code=200)
def all_by_status():
    try:
        return mdb.count_all_by_status()
    
    except Exception as e:
        raise HTTPException(status_code=500,detail=str(e))

@router.get("/reports/top-agent",status_code=200)
def top_agent():
    try:
        return mdb.get_top_agent()
    except Exception as e:
        raise HTTPException(status_code=500,detail=str(e))
