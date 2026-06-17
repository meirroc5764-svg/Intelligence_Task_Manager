from mysql import connector

class DBConnection:
    def __init__(self):
        self.host = "localhost"
        self.user = "root"
        self.password = "1234"
        self.database = "Intelligence_db"
    
    def get_connection(self):
        return connector.connect(
        host = self.host,
        user = self.user,
        password = self.password,
        dataabase = self.database
        )
    
    def create_database(self):
        conn = None
        try:    
            conn = connector.connect(
            host = self.host,
            user = self.user,
            password = self.password,
            )


            cursor = conn.cursor()

            cursor.execute("CREATE DATABASE IF NOT EXISTS Intelligence_db")

            conn.commit()

            
            return "create database finish"
        
        except Exception as e:
            raise e
        
        finally:
            if conn:
                cursor.close()
                conn.close()




if __name__ == "__main__":
    dbc = DBConnection()
    dbc.create_database()
