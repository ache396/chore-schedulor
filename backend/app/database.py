from sqlalchemy import create_engine

class SQLDatabase:
    def __init__(self, user, password, host, port, db_name):
        self.database_url = f"postgresql://{user}:{password}@{host}:{port}/{db_name}"
        self.engine = create_engine(self.database_url)
