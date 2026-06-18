from db_connection import DBConnection



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

    def deactivate_agent(self,id):
        conn = None
        try:
            conn = dbc.get_connection()

            cursor = conn.cursor()
            cursor.execute("UPDATE agents SET  is_active = %s WHERE id = %s ",(False,id))

            conn.commit()

            return "apdate sucssfule"
        except Exception as e:
            raise e
        
        finally:
            if conn:
                cursor.close()
                conn.close()    

    def increment_completed(self,id):
        conn = None
        try:
            conn = dbc.get_connection()

            cursor = conn.cursor()

            cursor.execute("SELECT completed_missions FROM agents WHERE id = %s",(id,))

            my_num = cursor.fetchone()[0]

            new_num = my_num +1

            cursor.execute("UPDATE agents SET completed_missions = %s  WHERE id = %s",(new_num,id))
            
            conn.commit()

            return "update completed_missions num sucssfule"

        except Exception as e:
            raise e
        
        finally:
            if conn:
                cursor.close()
                conn.close() 

    def increment_failed(self,id):
        conn = None
        try:
            conn = dbc.get_connection()

            cursor = conn.cursor()

            cursor.execute("SELECT completed_missions FROM agents WHERE id = %s",(id,))

            my_num = cursor.fetchone()[0]

            new_num = my_num +1

            cursor.execute("UPDATE agents SET failed_missions = %s  WHERE id = %s",(new_num,id))
            
            conn.commit()

            return "update failed_missions num sucssfule"

        except Exception as e:
            raise e
        
        finally:
            if conn:
                cursor.close()
                conn.close()


    def get_agent_performance(self):
        conn = None
        try:
            conn = dbc.get_connection()

            cursor = conn.cursor()

            cursor.execute("SELECT SUM(completed_missions) FROM agents ")

            num_completed_missions = cursor.fetchone()[0]

            cursor.execute("SELECT SUM(failed_missions)  FROM agents ")

            num_failed_missions = cursor.fetchone()[0]

            total = num_completed_missions + num_failed_missions

            success_rate = round((num_completed_missions/total) * 100,2)

            return {"completed":num_completed_missions, "failed":num_failed_missions, "total":total, "success_rate":success_rate }

        except Exception as e:
            raise e
        
        finally:
            if conn:
                cursor.close()
                conn.close()
    
    def count_active_agents(self):
        conn = None
        try:
            conn = dbc.get_connection()

            cursor = conn.cursor()

            cursor.execute("SELECT COUNT(*) FROM agents WHERE is_active = %s",(True,))

            all_active = cursor.fetchone()[0]

            return all_active
        
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
    # print(adb.create_agent(agent))
    print(adb.get_all_agents())
    # print(adb.get_agent_by_id(2))
    # print(adb.update_agent(1,agent))
    # print(adb.increment_completed(1))
    print(adb.get_agent_performance())
    print(adb.count_active_agents())

