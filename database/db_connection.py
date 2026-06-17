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
        database = self.database
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

    def create_tables(self):
        conn = None
        try:
            conn = self.get_connection()

            cursor = conn.cursor()

            cursor.execute("CREATE TABLE IF NOT EXISTS agents("
            "id INT AUTO_INCREMENT PRIMARY KEY,"
            "name VARCHAR(50) NOT NULL,"
            "specialty VARCHAR(50) NOT NULL," 
            "is_active BOOLEAN DEFAULT TRUE,"
            "completed_missions	INT DEFAULT 0," 
            "failed_missions INT DEFAULT 0,"
            "agent_rank	ENUM('Junior','Senior','Commandor'))")

            conn.commit()
    

            cursor.execute("CREATE TABLE IF NOT EXISTS missions(" \
            "id INT AUTO_INCREMENT PRIMARY KEY," \
            "title VARCHAR(50) NOT NULL," \
            "description TEXT NOT NULL," \
            "location VARCHAR(50) NOT NULL," \
            "difficulty	INT NOT NULL," \
            "importance INT NOT NULL," \
            "status ENUM('NEW', 'ASSIGNED', 'IN_PROGRESS', 'COMPLETED', 'FAILED', 'CANCELLED') DEFAULT 'NEW' ," \
            "risk_level	VARCHAR(50) NOT NULL," \
            "assigned_agent_id INT DEFAULT NULL)")

            conn.commit()

            return "create tables"
        
        except Exception as e:
            raise e
        
        finally:
            if conn:
                cursor.close()
                conn.close()


if __name__ == "__main__":
    dbc = DBConnection()
    dbc.create_database()
    dbc.create_tables()