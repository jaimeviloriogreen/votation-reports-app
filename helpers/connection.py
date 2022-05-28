import psycopg2

class Connection:
    cursor = None
    connect = None
    
    def __init__(self, dataConnection) -> None:
        try:
            self.connect = psycopg2.connect(
                host = dataConnection['host'],
                dbname = dataConnection['dbname'],
                user = dataConnection['user'],
                password = dataConnection['password'],
                port = dataConnection['port']
            )
        
        except Exception as error:
            print(f"Error: {error}")
        
    


