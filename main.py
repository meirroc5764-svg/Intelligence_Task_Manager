from routes.agent_routes import router as agent_routes
from routes.mission_routes import router as mission_routes
from routes.report_routes import router as report_routes
from database.db_connection import DBConnection

from fastapi import FastAPI
import uvicorn

dbc = DBConnection()
app = FastAPI()


app.include_router(agent_routes)
app.include_router(mission_routes)
app.include_router(report_routes)








if __name__=="__main__":
    dbc.create_database()
    dbc.create_tables()
    uvicorn.run("main:app",reload=True)