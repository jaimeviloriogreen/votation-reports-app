import psycopg2

class Connection:
    def __init__(self, dataConnection) -> None:
        try:
            self.connect = psycopg2.connect(
                host = dataConnection['host'],
                dbname = dataConnection['dbname'],
                user = dataConnection['user'],
                password = dataConnection['password'],
                port = dataConnection['port']
            )
            
            self.cur = self.connect.cursor()
        except Exception as error:
            print(f"Error: {error}")
        
    def getCandidates(self):
        self.cur.execute(
        """
            SELECT 
                candidatos.id, nombre, apellido, posiciones AS aspiraciones 
            FROM candidatos 
                INNER JOIN candidaturas 
            ON 
                candidaturas.id = candidatos.aspiraciones;
        """
        )
        
        return self.cur.fetchall()
    
    def numberOfVoteCast(self):
        self.cur.execute("SELECT COUNT(*) FROM voto")
        return self.cur.fetchone()
    
    def votesByGender(self):
        self.cur.execute(
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
        return self.cur.fetchall()
    
    def votesByCandidates(self):
        self.cur.execute(
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
        return self.cur.fetchall()
    
    def closeConnection(self):
        self.cur.close()
        self.connect.close()


