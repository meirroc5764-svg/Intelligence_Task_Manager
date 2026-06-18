from pydantic import BaseModel


from database.db_connection import DBConnection



dbc = DBConnection()

class AgentDB:
    def __init__(self):
        pass

    def create_agent(self,data):
        conn = None
        try:    
            conn = dbc.get_connection()

            cursor = conn.cursor()

            cursor.execute("INSERT INTO agents(name, specialty, agent_rank) VALUES(%s,%s,%s)",(data["name"],data["specialty"],data["agent_rank"]))

            conn.commit()

            new_agent_id = cursor.lastrowid

            cursor.execute("SELECT * FROM agents WHERE id = %s",(new_agent_id,))

            new_agent = cursor.fetchone()
            
            return new_agent
        
        except Exception as e:
            raise e
    
        finally:
            if conn:
                cursor.close()
                conn.close()
    
    def get_all_agents(self):
        conn = None
        try:
            conn = dbc.get_connection()

            cursor = conn.cursor()

            cursor.execute("SELECT * FROM agents")

            all_data = cursor.fetchall()

            return all_data
        
        except Exception as e:
            raise e

        finally:
            if conn:
                cursor.close()
                conn.close()


    def get_agent_by_id(self,id):
        conn = None
        try:
            conn = dbc.get_connection()

            cursor = conn.cursor()

            cursor.execute("SELECT * FROM agents WHERE id = %s",(id,))

            my_agent = cursor.fetchone()
            if not my_agent:
                return None

            return my_agent
        
        except Exception as e:
            raise e
        
        finally:
            if conn:
                cursor.close()
                conn.close()

    
    def update_agent(self,id,data):
        conn = None
        try:
            conn = dbc.get_connection()

            cursor = conn.cursor()
            for key,value in data.items():
                data_update = f"UPDATE agents SET {key} = %s WHERE id = %s"
        
                cursor.execute(data_update,(value,id))
                conn.commit()
        
            return "change a agent"
        except Exception as e:
            raise e
        
        finally:
            if conn:
                cursor.close()
                conn.close()

if __name__=="__main__":
    adb = AgentDB()
    agent = {"name":"meir",
             "specialty":"program",
             "agent_rank":"junior"}
    print(adb.create_agent(agent))
    print(adb.get_all_agents())
    # print(adb.get_agent_by_id(2))
    print(adb.update_agent(1,agent))

