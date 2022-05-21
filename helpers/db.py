import psycopg2

class Connection:
    __hostname = "localhost"
    __database = "votaciones_puesto_municipal"
    __username = "jaimeviloriogreen"
    __password = "Provervios12:23"
    __portID = 5432
    
    def __init__(self) -> None:
        try:
            self.connect = psycopg2.connect(
                host = self.__hostname,
                dbname = self.__database,
                user = self.__username,
                password = self.__password,
                port = self.__portID
            )
            
            self.cur = self.connect.cursor()
        except Exception as error:
            print(f"Error: {error}")
        
    
    def getCandidates(self):
        self.cur.execute("SELECT id, nombre, apellido, aspiraciones FROM candidatos")
        return self.cur.fetchall()
    
    def numberOfVoteCast(self):
        self.cur.execute("SELECT COUNT(*) FROM voto")
        return self.cur.fetchone()
    
    def closeConnection(self):
        self.cur.close()
        self.connect.close()


