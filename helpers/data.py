from helpers.connection import Connection

class Data(Connection):
    def __init__(self, dataConnection) -> None:
        super().__init__(dataConnection)

    def getCandidates(self):
        try:
            self.cursor = self.connect.cursor()
            self.cursor.execute(
            """
                SELECT 
                    candidatos.id, nombre, apellido, posiciones AS aspiraciones 
                FROM candidatos 
                    INNER JOIN candidaturas 
                ON 
                    candidaturas.id = candidatos.aspiraciones;
            """
            )
            result = self.cursor.fetchall()
            return result
        except Exception as error:
            print(f"Error: {error}")
        finally:
            self.closeConnection()
           
    def numberOfVoteCast(self):
        try:
            self.cursor = self.connect.cursor()
            self.cursor.execute("SELECT COUNT(*) FROM voto")
            result =  self.cursor.fetchone()
            return result
        except Exception as error:
            print(f"Error: {error}")
        finally:
            self.closeConnection()
    
    def votesByGender(self):
        try:
            self.cursor = self.connect.cursor()
            self.cursor.execute(
            """
                SELECT 
                    sexo, COUNT(sexo) 
                FROM 
                    voto 
                INNER JOIN votantes 
                ON 
                    voto.votante = votantes.id GROUP BY(sexo);
            """
            )
            result = self.cursor.fetchall()
            return result
        except Exception as error:
            print(f"Error: {error}")
        finally:
            self.closeConnection()
    
    def votesByCandidates(self):
        try:
            self.cursor = self.connect.cursor()
            self.cursor.execute(
            """
                SELECT 
                    nombre||' '||apellido, 
                    COUNT(votante) 
                FROM 
                    voto 
                INNER JOIN candidatos 
                ON 
                    candidatos.id = voto.candidato 
                GROUP BY(nombre||' '||apellido) ORDER BY(COUNT(votante)) DESC;
            """
            )
            
            result = self.cursor.fetchall()
            return result
        
        except Exception as error:
            print(f"Error: {error}")
        finally:
            self.closeConnection()
    
    def closeConnection(self):
        if self.cursor is not None:
            self.cursor.close()
        if self.connect is not None:
            self.connect.close()