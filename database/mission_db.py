from database.db_connection import DBConnection
from database.agent_db import AgentDB
dbc = DBConnection()
adb = AgentDB()


class MissionDB:
    def __init__(self):
        pass
    
    def risk_level(self,difficulty,importance):

        my_risk_level = difficulty * 2 + importance

        if 0 <= my_risk_level < 10:
            my_risk_level = "LOW"
        
        elif 10 <= my_risk_level < 18:
            my_risk_level = "MEDIUM"
        
        elif 18 <= my_risk_level < 25:
            my_risk_level = "HIGH"
        
        elif my_risk_level >= 25:
            my_risk_level = "CRITICAL"

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

        
        conn = None
        try:
            conn = dbc.get_connection()

            cursor = conn.cursor()

            cursor.execute("UPDATE missions SET assigned_agent_id = %s WHERE id = %s",(a_id,m_id))

            conn.commit()

            cursor.execute("UPDATE missions SET status = %s WHERE id = %s",(m_id,))

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
    
    
    
    def get_open_missions_by_agent(self,id):
        conn = None
        try:
            conn = dbc.get_connection()

            cursor = conn.cursor()

            cursor.execute("SELECT * FROM missions WHERE assigned_agent_id = %s AND status IN (%s,%s)",(id,"ASSIGNED","IN_PROGRESS"))

            my_mission = cursor.fetchall()

            if not my_mission:
                return None

            return my_mission
        
        
        except Exception as e:
            raise e
        
        finally:
            if conn:
                cursor.close()
                conn.close()
    

    def count_all_missions(self):
        conn = None
        try:
            conn = dbc.get_connection()

            cursor = conn.cursor()

            cursor.execute("SELECT COUNT(*) FROM missions")

            all_data = cursor.fetchone()[0]

            return all_data
        
        except Exception as e:
            raise e

        finally:
            if conn:
                cursor.close()
                conn.close()
    
    
    def count_by_status(self,status):
        conn = None
        try:
            conn = dbc.get_connection()

            cursor = conn.cursor()

            cursor.execute("SELECT COUNT(*) FROM missions WHERE status = %s",(status,))

            all_data = cursor.fetchone()[0]

            return all_data
        
        except Exception as e:
            raise e

        finally:
            if conn:
                cursor.close()
                conn.close()
    
    
    def count_open_missions(self):
        conn = None
        try:
            conn = dbc.get_connection()

            cursor = conn.cursor()

            cursor.execute("SELECT COUNT(*) FROM missions WHERE status = %s OR status = %s",("ASSIGNED","IN_PROGRESS"))

            all_data = cursor.fetchone()[0]

            return all_data
        
        except Exception as e:
            raise e

        finally:
            if conn:
                cursor.close()
                conn.close()


    def count_critical_missions(self):
        conn = None
        try:
            conn = dbc.get_connection()

            cursor = conn.cursor()

            cursor.execute("SELECT COUNT(*) FROM missions WHERE risk_level = %s",("CRITICAL",))

            all_data = cursor.fetchone()[0]

            return all_data
        
        except Exception as e:
            raise e

        finally:
            if conn:
                cursor.close()
                conn.close()
    

    def get_top_agent(self):
        conn = None
        try:
            conn = dbc.get_connection()

            cursor = conn.cursor(dictionary=True)

            cursor.execute("SELECT MAX(completed_missions) AS max FROM agents")

            max_num = cursor.fetchone()["max"]

            cursor.execute("SELECT * FROM agents WHERE completed_missions = %s",(max_num,))

            best_agent = cursor.fetchone()

            return best_agent
        
        except Exception as e:
            raise e

        finally:
            if conn:
                cursor.close()
                conn.close()


    def count_all_by_status(self,):
        conn = None
        try:
            conn = dbc.get_connection()

            cursor = conn.cursor()

            cursor.execute("SELECT status,COUNT(*)  FROM missions GROUP BY STATUS")

            all_data = cursor.fetchall()

            return all_data
        
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
    # print(mdb.risk_level(5,6))
    # print(mdb.create_mission(missions))
    print(mdb.get_all_missions())
    # print(mdb.get_mission_by_id(2))
    # print(mdb.assign_mission(1,5))
    # print(mdb.update_mission_status(2,"ASSIGNED"))
    # print(mdb.get_open_missions_by_agent(5))
    # print(mdb.count_all_missions())
    # print(mdb.count_by_status("new"))
    # print(mdb.count_open_missions())
    # print(mdb.count_critical_missions())
    # print(mdb.get_top_agent())
    print(mdb.count_all_by_status())