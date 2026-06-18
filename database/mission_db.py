from db_connection import DBConnection
from agent_db import AgentDB
dbc = DBConnection()
adb = AgentDB()


class MissionDB:
    def __init__(self):
        pass
    
    def risk_level(self,difficulty,importance):

        my_risk_level = difficulty * 2 + importance

        return my_risk_level


    def create_mission(self,data):
        conn = None

        my_risk_level = self.risk_level(data["difficulty"],data["importance"])
        try:    
            conn = dbc.get_connection()

            cursor = conn.cursor()

            cursor.execute("INSERT INTO missions(scription, locatitle, detion, difficulty, importance, risk_level) VALUES(%s,%s,%s,%s,%s,%s)",(data["scription"], data["locatitle"], data["detion"], data["difficulty"], data["importance"], my_risk_level))

            conn.commit()

            new_missions_id = cursor.lastrowid

            cursor.execute("SELECT * FROM  missions WHERE id = %s",(new_missions_id,))

            new_missions = cursor.fetchone()
            
            return new_missions
        
        except Exception as e:
            raise e
    
        finally:
            if conn:
                cursor.close()
                conn.close()
    
    
    def get_all_missions(self):
        conn = None
        try:
            conn = dbc.get_connection()

            cursor = conn.cursor(dictionary=True)

            cursor.execute("SELECT * FROM missions")

            all_data = cursor.fetchall()

            return all_data
        
        except Exception as e:
            raise e

        finally:
            if conn:
                cursor.close()
                conn.close()

    def get_mission_by_id(self,id):
        conn = None
        try:
            conn = dbc.get_connection()

            cursor = conn.cursor()

            cursor.execute("SELECT * FROM missions WHERE id = %s",(id,))

            my_mission = cursor.fetchone()

            if not my_mission:
                return None

            return my_mission
        
        except Exception as e:
            raise e
        
        finally:
            if conn:
                cursor.close()
                conn.close()

    def assign_mission(self,m_id, a_id):
        if not adb.get_agent_by_id(a_id):
            return "not fount a agent with this id"
        if not self.get_mission_by_id(m_id):
            return "not found a mission with this id"
        
        conn = None
        try:
            conn = dbc.get_connection()

            cursor = conn.cursor()

            cursor.execute("UPDATE missions SET assigned_agent_id = %s WHERE id = %s",(a_id,m_id))

            conn.commit()

            return "a mission assign"
        
        except Exception as e:
            raise e
        
        finally:
            if conn:
                cursor.close()
                conn.close()

    def update_mission_status(self,id, status):
        conn = None
        try:
            conn = dbc.get_connection()

            cursor = conn.cursor()

            cursor.execute("UPDATE missions SET status = %s WHERE id = %s",(status,id))

            conn.commit()

            return "a mission status change"
        
        except Exception as e:
            raise e
        
        finally:
            if conn:
                cursor.close()
                conn.close()
    
    
    
    


if __name__=="__main__":
    mdb = MissionDB()
    missions = {"scription":"hello world i am here,",
             "locatitle":"program",
             "detion":"junior",
             "difficulty":5,
             "importance":6}
    # print(mdb.create_mission(missions))
    print(mdb.get_all_missions())
    print(mdb.get_mission_by_id(2))
    print(mdb.assign_mission(1,5))