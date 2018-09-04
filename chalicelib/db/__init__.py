from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from chalicelib.con.config import connection_strings  # Not committed to VCS

__all__ = ["DatabaseConnection", "DatabaseSession"]

connection_string = connection_strings.get("prod")
engine = create_engine(connection_string)

class DatabaseConnection:
    def __enter__(self):
        self.conn = engine.connect()
        return self.conn

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.conn.close()

class DatabaseSession:
    def __enter__(self):
        self.session = Session(engine)
        self.session.expire_on_commit = False
        return self.session

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.close()
        self.session = None
